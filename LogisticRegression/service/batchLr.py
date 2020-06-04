import random
from math import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

class BatchLR:
    def __init__(self):
        self.intercept = random.random()
        self.coef = []

    def fit(self, inputs, outputs, alpha=0.001, noEpochs=1000):
        # inputs de forma [[feat1, feat2, ...], [feat1, feat2, ...], ...]
        self.coef = [random.random() for _ in range(len(inputs[0]) + 1)]
        for epoch in range(noEpochs):
            error = 0
            t0 = 0
            for i in range(len(inputs)):
                computed = sigmoid(self.eval(inputs[i], self.coef))
                for j in range(len(inputs[0])):
                    error += (computed - outputs[i]) * inputs[i][j]
                    t0 += computed - outputs[i]

            for j in range(0, len(inputs[0])):
                self.coef[j + 1] = self.coef[j + 1] - alpha * error / len(inputs)
            self.coef[0] = self.coef[0] - alpha * t0 / len(inputs)

        self.intercept = self.coef[0]
        self.coef = self.coef[1:]

    def eval(self, xi, coef):
        yi = self.intercept
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    def predictOneSample(self, sampleFeatures):
        threshold = 0.5
        coefficients = [self.intercept] + [c for c in self.coef]
        computedFloatValue = self.eval(sampleFeatures, coefficients)
        computed01Value = sigmoid(computedFloatValue)
        computedLabel = 0 if computed01Value < threshold else 1
        return computedLabel

    def predict(self, inTest):
        computedLabels = [self.predictOneSample(sample) for sample in inTest]
        return computedLabels

    def compute(self, inTest):
        coefficients = [self.intercept] + [c for c in self.coef]
        computedFloatValue = self.eval(inTest, coefficients)
        return sigmoid(computedFloatValue)