from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from repository.reader import Reader
from service.dataOps import split_data, extractFeatures, normalise
from service.myKMeans import myKMeans
from service.toolKM import tool


def main():
    data = datasets.load_iris()
    inputs = data['data']
    outputs = data['target']
    outputNames = data['target_names']
    featureNames = list(data['feature_names'])
    inputs = [[feat[featureNames.index('sepal length (cm)')], feat[featureNames.index('sepal width (cm)')],
               feat[featureNames.index('petal length (cm)')], feat[featureNames.index('petal width (cm)')]] for feat in
              inputs]

    trainInputs, trainOutputs, testInputs, testOutputs = split_data(inputs, outputs)
    normalisedTrain, normalisedTest = normalise(trainInputs, testInputs)
    outputsByName = [outputNames[value] for value in testOutputs]
    print("Iris dataset:")
    tool(normalisedTrain, normalisedTest, outputsByName, outputNames, 3)
    regressor = LogisticRegression(max_iter=1000, multi_class='ovr')
    regressor.fit(normalisedTrain, trainOutputs)
    tool_output = regressor.predict(normalisedTest)
    print("Acc supervised: ", accuracy_score(testOutputs, tool_output))

    reader = Reader("data/reviews_mixed.csv")
    inputs2, outputs2, labelNames = reader.read()
    trainInputs2, trainOutputs2, testInputs2, testOutputs2 = split_data(inputs2, outputs2)
    trainFeatures, testFeatures = extractFeatures(trainInputs2, testInputs2)
    print("Emotions dataset:")
    tool(trainFeatures, testFeatures, testOutputs2, labelNames, 2)

    featureArr = trainFeatures.toarray()
    km = myKMeans(1000)
    km.fit(featureArr, 2)
    computed = km.predict(testFeatures.toarray())
    computedLabels = [labelNames[i] for i in computed]
    print("Acc manual: ", accuracy_score(testOutputs2, computedLabels))

main()