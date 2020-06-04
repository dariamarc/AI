from math import sqrt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from service.myRegression import bivariateRegression
import matplotlib.pyplot as plt


class LeastSquaresMethod:
    def __init__(self):
        self.trainInputs = []
        self.trainOutputs = []
        self.testInputs = []
        self.testOutputs = []

    # split the data into training data and test data
    def split_data(self, inputs, outputs):
        np.random.seed(5)
        indexes = [i for i in range(len(inputs[0]))]
        trainSample = np.random.choice(indexes, int(0.8 * len(inputs[0])), replace=False)
        testSample = [i for i in indexes if not i in trainSample]

        for idx_input in range(len(inputs)):
            self.trainInputs.append([inputs[idx_input][i] for i in trainSample])
        self.trainOutputs = [outputs[i] for i in trainSample]

        for idx_input in range(len(inputs)):
            self.testInputs.append([inputs[idx_input][i] for i in testSample])
        self.testOutputs = [outputs[i] for i in testSample]


    def plot_learnt_model(self, w0, w1, w2):
        # prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)
        noOfPoints = 1000
        xref1 = []
        xref2 = []
        val1 = min(self.trainInputs[0])
        val2 = min(self.trainInputs[1])
        step1 = (max(self.trainInputs[0]) - min(self.trainInputs[0])) / noOfPoints
        step2 = (max(self.trainInputs[1]) - min(self.trainInputs[1])) / noOfPoints
        for i in range(1, noOfPoints):
            xref1.append(val1)
            xref2.append(val2)
            val1 += step1
            val2 += step2
        yref = [w0 + w1 * xref1[i] + w2 * xref2[i] for i in range(len(xref1))]

        plt.axes(projection='3d')
        plt.plot(self.trainInputs[0], self.trainInputs[1], self.trainOutputs, 'ro',
                 label='training data')  # train data are plotted by red and circle sign
        plt.plot(xref1, xref2, yref, 'b-', label='learnt model')  # model is plotted by a blue line
        plt.title('train data and the learnt model')
        plt.xlabel('GDP capita')
        plt.ylabel('Freedom')
        plt.legend()
        plt.show()


    def least_squares_method(self, inputs, outputs):
        self.split_data(inputs, outputs)
        regres = bivariateRegression()
        regres.fit(self.trainInputs, self.trainOutputs)
        print("f(x, w) = " + str(regres.intercept) + " + " + str(regres.coef_[0]) + " * x1 + " + str(regres.coef_[1]) + " * x2")

        # training data preparation (the sklearn linear model requires as input training data as noSamples x noFeatures array; in the current case, the input must be a matrix of len(trainInputs) lineas and one columns (a single feature is used in this problem))
        xx = [[self.trainInputs[0][i], self.trainInputs[1][i]] for i in range(len(self.trainInputs[0]))]

        # model initialisation
        regressor = linear_model.LinearRegression()
        # training the model by using the training inputs and known training outputs
        regressor.fit(xx, self.trainOutputs)
        # save the model parameters
        w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
        print("sklearn: w0 = " + str(w0) + " w1 = " + str(w1) + " w2 = " + str(w2))

        # self.plot_learnt_model(regres.intercept, regres.coef_[0], regres.coef_[1])
        results = regres.predict(self.testInputs)

        error = self.compute_error(self.testOutputs, results)
        print("error: " + str(error))
        print("sklearn error: " + str(mean_squared_error(self.testOutputs, results)))


    def compute_error(self, realOutputs, predictedOutputs):
        error = 0.0
        for t1, t2 in zip(predictedOutputs, realOutputs):
            error += (t1 - t2) ** 2
        return error / len(realOutputs)