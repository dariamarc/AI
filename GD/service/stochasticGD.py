import random

class SGD:
    def __init__(self, alpha, noEpochs):
        self.alpha = alpha
        self.noEpochs = noEpochs
        self.intercept = random.random()
        self.coefs = []

    # simple stochastic GD
    def fit(self, inputs, outputs):
        self.coefs = [random.random() for _ in range(len(inputs) + 1)]
        for epoch in range(self.noEpochs):
            # TBA: shuffle the trainind examples in order to prevent cycles
            for i in range(len(inputs[0])): # for each sample from the training data
                ycomputed = self.eval(inputs, i)     # estimate the output
                crtError = ycomputed - outputs[i]     # compute the error for the current sample
                for j in range(0, len(inputs)):   # update the coefficients
                    self.coefs[j] = self.coefs[j] - self.alpha * crtError * inputs[j][i]
                self.coefs[len(inputs)] = self.coefs[len(inputs)] - self.alpha * crtError

        self.intercept = self.coefs[-1]
        self.coefs = self.coefs[:-1]

    def eval(self, inputs, idx):
        yi = self.coefs[-1]
        for j in range(len(inputs)):
            yi += self.coefs[j] * inputs[j][idx]
        return yi

    def predict(self, input):
        # ia toate inputurile si calculeaza pentru fiecare index valoarea
        yComputed = []
        for i in range(len(input[0])):
            yComputed.append(self.eval(input, i))

        return yComputed