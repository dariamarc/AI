import random


class BatchGD:
    def __init__(self, alpha, noEpochs):
        self.alpha = alpha
        self.noEpochs = noEpochs
        self.intercept = random.random()
        self.coefs = []

    def fit(self, inputs, outputs):
        self.coefs = [random.random() for _ in range(len(inputs) + 1)]
        for epoch in range(self.noEpochs):
            error = 0
            t0 = 0
            for i in range(len(inputs[0])):
                computed = self.eval(inputs, i)
                for j in range(len(inputs)):
                    error += (computed - outputs[i]) * inputs[j][i]
                    t0 += computed - outputs[i]

            for j in range(0, len(inputs)):
                self.coefs[j] = self.coefs[j] - self.alpha * error / len(inputs[0])
            self.coefs[len(inputs)] = self.coefs[len(inputs)] - self.alpha * t0 / len(inputs[0])

        self.intercept = self.coefs[-1]
        self.coefs = self.coefs[:-1]


    def eval(self, inputs, idx):
        # ia toate input-urile si indexul pentru care se calculeaza
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