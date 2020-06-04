import numpy as np

def flatten(mat):
    x = []
    for line in mat:
        values = []
        for el in line:
            for e in el:
                for i in e:
                    values.append(i)
        x.append(values)
    return x

def flatten2(mat):
    x = []
    for line in mat:
        values = []
        for el in line:
            for e in el:
                values.append(e)
        x.append(values)

    return x

def split_data(inputs, outputs):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]
    return trainInputs, testInputs, trainOutputs, testOutputs

def normalisation(trainData, testData):
    # scaling
    scaledTrain = []
    scaledTest = []
    for input in trainData:
        minValue = min(input)
        maxValue = max(input)
        scaledInput = [(val - minValue) / (maxValue - minValue) for val in input]
        scaledTrain.append(scaledInput)
    for input in testData:
        minValue = min(input)
        maxValue = max(input)
        scaledInput = [(val - minValue) / (maxValue - minValue) for val in input]
        scaledTest.append(scaledInput)

    #zero centralisation
    normalisedTrain = []
    for input in scaledTrain:
        meanValue = sum(input) / len(input)
        centeredInput = [val - meanValue for val in input]
        normalisedTrain.append(centeredInput)

    normalisedTest = []
    for input in scaledTest:
        meanValue = sum(input) / len(input)
        centeredInput = [val - meanValue for val in input]
        normalisedTest.append(centeredInput)

    return normalisedTrain, normalisedTest

def shuffle(inputs, outputs):
    noData = len(inputs)
    permutation = np.random.permutation(noData)
    newInputs = []
    newOutputs = []
    for nr in permutation:
        newInputs.append(inputs[nr])
        newOutputs.append(outputs[nr])

    return newInputs, newOutputs
