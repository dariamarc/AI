from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

from repo.reader import Reader
from service.dataOps import shuffle, split_data, flatten, normalisation, flatten2
import numpy as np

from service.myANN import NeuralNetwork


def faceEmotionsPredict():
    reader = Reader()
    inputs, outputs = reader.readFaces()
    inputs, outputs = shuffle(inputs, outputs)
    trainInputs, testInputs, trainOutputs, testOutputs = split_data(inputs, outputs)
    simpleOutputs_train = []
    for i in trainOutputs:
        if i[0] == 1:
            simpleOutputs_train.append(1)
        else:
            simpleOutputs_train.append(0)
    simpleOutputs_test = []
    for i in testOutputs:
        if i[0] == 1:
            simpleOutputs_test.append(1)
        else:
            simpleOutputs_test.append(0)

    trainInputs = [e.tolist() for e in trainInputs]
    testInputs = [e.tolist() for e in testInputs]
    trainInputs = flatten2(trainInputs)
    testInputs = flatten2(testInputs)
    normalisedTrain, normalisedTest = normalisation(trainInputs, testInputs)

    print('My ANN face emotions..............')
    net = NeuralNetwork(1, 4, 20)
    net.fit(normalisedTrain, simpleOutputs_train, 0.01)
    computed = net.predict(normalisedTest)

    error = 0.0
    for t1, t2 in zip(computed, simpleOutputs_test):
        if (t1 != t2):
            error += 1

    print("Manual error: " + str(error / len(trainInputs)))