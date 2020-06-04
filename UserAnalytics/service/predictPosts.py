import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import neural_network

def split_data(inputs, outputs, outputsImage, outputsText):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    outputsTrainImage = [outputsImage[i] for i in trainSample]
    outputsTrainText = [outputsText[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]
    outputsTestImage = [outputsImage[i] for i in testSample]
    outputsTestText = [outputsText[i] for i in testSample]
    return trainInputs, testInputs, trainOutputs, testOutputs, outputsTrainImage, outputsTestImage, outputsTrainText, outputsTestText


def extractFeatures(trainInputs, testInputs):
    vectorizer = TfidfVectorizer(max_features=600)
    trainFeatures = vectorizer.fit_transform(trainInputs)
    testFeatures = vectorizer.transform(testInputs)
    return trainFeatures, testFeatures


def flatten(mat):
    x = []
    for line in mat:
        values = []
        for el in line:
            for e in el:
                values.append(e)
        x.append(values)
    return x


class MyPredictor:
    def predict(self, inputs, outputs, outputsImages, outputsTexts):
        trainInputs, testInputs,trainOutputs, testOutputs, trainOutImages, testOutImages, trainOutText, testOutText = split_data(inputs, outputs, outputsImages, outputsTexts)

        textInputsTrain = [trainInputs[i][0] for i in range(len(trainInputs))]
        textInputsTest = [testInputs[i][0] for i in range(len(testInputs))]
        labels = ['positive', 'negative']
        trainFeatures, testFeatures = extractFeatures(textInputsTrain, textInputsTest)
        imageInputsTrain = [trainInputs[i][1] for i in range(len(trainInputs))]
        imageInputsTest = [testInputs[i][1] for i in range(len(testInputs))]

        trainImages = []
        for trainImage in imageInputsTrain:
            image = Image.open('data/' + trainImage).resize((30, 30))
            data = np.asarray(image)
            trainImages.append(data)

        testImages = []
        for testImage in imageInputsTest:
            image = Image.open('data/' + testImage).resize((30, 30))
            data = np.asarray(image)
            testImages.append(data)

        trainFlatten = flatten(trainImages)
        testFlatten = flatten(testImages)

        # predict labels for text
        unsupervisedClassifier = KMeans(n_clusters=2, max_iter=1000, random_state=0)
        unsupervisedClassifier.fit(trainFeatures)
        computedTestIndexes = unsupervisedClassifier.predict(testFeatures)
        computedTestOutputs = [labels[value] for value in computedTestIndexes]

        #predict labels for image
        classifier = neural_network.MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', max_iter=100,
                                                  solver='sgd',
                                                  verbose=10, random_state=1, learning_rate_init=0.01)

        classifier.fit(trainFlatten, trainOutImages)
        predictedLabels = classifier.predict(testFlatten)
        #print(predictedLabels)

        #clasificator pentru text si imagine
        lastTrain = []
        for i in range(len(trainOutputs)):
            lastTrain.append([trainOutText[i], trainOutImages[i]])

        trainIn = []
        for i in lastTrain:
            val = []
            for j in i:
                if j == 'negative':
                    val.append(0)
                else:
                    val.append(1)
            trainIn.append(val)


        predictedLabels = predictedLabels.tolist()
        lastTest = []
        for i in range(len(predictedLabels)):
            lastTest.append([computedTestOutputs[i], predictedLabels[i]])

        testIn = []
        for i in lastTest:
            val = []
            for j in i:
                if j == 'negative':
                    val.append(0)
                else:
                    val.append(1)
            testIn.append(val)

        classifier2 = neural_network.MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', max_iter=100,
                                                  solver='sgd',
                                                  verbose=10, random_state=1, learning_rate_init=0.01)

        classifier2.fit(trainIn, trainOutputs)
        predicted = classifier2.predict(testIn)

        print(predicted)
        error = 0.0
        for t1, t2 in zip(predicted, testOutputs):
            if (t1 != t2):
                error += 1

        print("Prediction error: " + str(error / len(trainIn)))
