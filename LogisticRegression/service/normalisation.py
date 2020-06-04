from sklearn.preprocessing import StandardScaler


class Normalisation:
    def standardisation(self, trainInputs, testInputs):
        resultTrain = []
        resultTest = []
        for input_idx in range(len(trainInputs)):
            meanValue = sum(trainInputs[input_idx]) / len(trainInputs[input_idx])
            stdDevValue = (1 / len(trainInputs[input_idx]) * sum([(val - meanValue) ** 2 for val in trainInputs[input_idx]])) ** 0.5
            normalisedInputTrain = [(val - meanValue) / stdDevValue for val in trainInputs[input_idx]]
            normalisedInputTest = [(val - meanValue) / stdDevValue for val in testInputs[input_idx]]
            resultTrain.append(normalisedInputTrain)
            resultTest.append(normalisedInputTest)
        return resultTrain, resultTest


    def tool_normalisation(self, trainData, testData):
        scaler = StandardScaler()
        if not isinstance(trainData[0], list):
            # encode each sample into a list
            trainData = [[d] for d in trainData]
            testData = [[d] for d in testData]

            scaler.fit(trainData)  # fit only on training data
            normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
            normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

            # decode from list to raw values
            normalisedTrainData = [el[0] for el in normalisedTrainData]
            normalisedTestData = [el[0] for el in normalisedTestData]
        else:
            scaler.fit(trainData)  # fit only on training data
            normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
            normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
        return normalisedTrainData, normalisedTestData