import numpy as np
from sklearn.linear_model import LogisticRegression

from service.batchLr import BatchLR
from service.lr import MyLogisticRegression
from service.normalisation import Normalisation
from sklearn.metrics import accuracy_score

class LR:
    def __init__(self):
        self.trainInputs = []
        self.trainOutputs = []
        self.testInputs = []
        self.testOutputs = []

    def splitData(self, inputs, outputs):
        np.random.seed(5)
        indexes = [i for i in range(len(inputs))]
        trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
        testSample = [i for i in indexes if not i in trainSample]

        self.trainInputs = [inputs[i] for i in trainSample]
        self.trainOutputs = [outputs[i] for i in trainSample]
        self.testInputs = [inputs[i] for i in testSample]
        self.testOutputs = [outputs[i] for i in testSample]

    def lr(self, inputs, outputs, features, outputNames):
        self.splitData(inputs, outputs)
        norm = Normalisation()
        self.trainInputs, self.testInputs = norm.tool_normalisation(self.trainInputs, self.testInputs)

        logistic = MyLogisticRegression()
        batch = BatchLR()
        # avem 3 output-uri posibile: 0, 1, 2
        # trebuie reduse la 3 probleme de clasificare binara
        # output-urile sunt modificate astfel incat sa fie doar valori de 0 si 1
        labels = set(outputs)
        computed = []
        computedBatch = []
        for label in labels:
            newOutputs = [1 if p == label else 0 for p in self.trainOutputs]
            batch.fit(self.trainInputs, newOutputs)
            logistic.fit(self.trainInputs, newOutputs)
            w0, w1, w2, w3, w4 = logistic.intercept_, logistic.coef_[0], logistic.coef_[1], logistic.coef_[2], logistic.coef_[3]
            print('Learnt model for label ' + str(label) + ' is : ' + str(w0) + ' + ' + str(w1) + ' * feat1 + ' + str(w2) + ' * feat2 + ' + str(w3) + ' * feat3 + ' + str(w4) + ' * feat4')
            # valorile care au iesit in urma aplicarii modelului invatat si a functiei sigmoid pentru fiecare
            # exemplu de test
            computedValues = [logistic.compute(input) for input in self.testInputs]
            computed.append(computedValues)
            computedBatch.append([batch.compute(input) for input in self.testInputs])
            print(computedValues)
            #print(newOutputs)

        # lista de computed la final arata asa
        # [[c1_label1, c2_label1, ...], [c1_label2, c2_label2, ...], [c1_label3, c2_label3, ...]]
        # trebuie sa iau maximul pentru fiecare c pentru a stabili care label ii corespunde
        computedOutputs = []
        for i in range(len(computed[0])):
            maxVal = computed[0][i]
            label = 0
            for j in range(len(computed)):
                # j parcurge label-urile
                # i parcurge exemplele pentru care s-au calculat output-uri
                if(computed[j][i] > maxVal):
                    maxVal = computed[j][i]
                    label = j
            computedOutputs.append(label)

        outputsBatch = []
        for i in range(len(computedBatch[0])):
            maxVal = computedBatch[0][i]
            label = 0
            for j in range(len(computedBatch)):
                # j parcurge label-urile
                # i parcurge exemplele pentru care s-au calculat output-uri
                if (computedBatch[j][i] > maxVal):
                    maxVal = computedBatch[j][i]
                    label = j
            outputsBatch.append(label)

        print('Computed labels (manual) : ')
        print([outputNames[l] for l in computedOutputs])
        print('Computed labels (manual) with BATCH: ')
        print([outputNames[l] for l in outputsBatch])
        print('Real labels : ')
        print([outputNames[l] for l in self.testOutputs])

        print("Error stochastic:")
        self.error(self.testOutputs, computedOutputs)
        print("Error batch:")
        self.error(self.testOutputs, outputsBatch)

        # using tool
        regressor = LogisticRegression(max_iter=1000, multi_class='ovr')
        regressor.fit(self.trainInputs, self.trainOutputs)
        tool_output = regressor.predict(self.testInputs)
        print("Error sklearn:")
        self.error(self.testOutputs, tool_output)

    def error(self, testOutputs, computedTestOutputs):
        error = 0.0
        for t1, t2 in zip(computedTestOutputs, testOutputs):
            if (t1 != t2):
                error += 1

        toolError = 1 - accuracy_score(testOutputs, computedTestOutputs)
        print('Manual error : ' + str(error / len(testOutputs)))
        print('Tool error : ' + str(toolError))
