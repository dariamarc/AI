import random
from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y, learningRate=0.001, noEpochs=1000):
        self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]
        for epoch in range(noEpochs):
            for i in range(len(x)):
                ycomputed = sigmoid(self.eval(x[i], self.coef_))
                crtError = ycomputed - y[i]
                for j in range(0, len(x[0])):
                    self.coef_[j + 1] = self.coef_[j + 1] - learningRate * crtError * x[i][j]
                self.coef_[0] = self.coef_[0] - learningRate * crtError * 1

        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]

    def eval(self, xi, coef):
        yi = coef[0]
        for j in range(len(xi)):
            yi += coef[j + 1] * xi[j]
        return yi

    def predictOneSample(self, sampleFeatures):
        threshold = 0.5
        coefficients = [self.intercept_] + [c for c in self.coef_]
        computedFloatValue = self.eval(sampleFeatures, coefficients)
        computed01Value = sigmoid(computedFloatValue)
        computedLabel = 0 if computed01Value < threshold else 1
        return computedLabel

    def predict(self, inTest):
        computedLabels = [self.predictOneSample(sample) for sample in inTest]
        return computedLabels

    def compute(self, inTest):
        coefficients = [self.intercept_] + [c for c in self.coef_]
        computedFloatValue = self.eval(inTest, coefficients)
        return sigmoid(computedFloatValue)
