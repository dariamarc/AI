import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from mpl_toolkits import mplot3d
from service.batchGD import BatchGD
from service.normalisation import Normalisation
from service.stochasticGD import SGD
import matplotlib.pyplot as plt

class GradientDescentMethod:
    def __init__(self, alpha, noEpochs):
        self.alpha = alpha
        self.noEpochs = noEpochs
        self.trainInputs = []
        self.trainOutputs = []
        self.testInputs = []
        self.testOutputs = []

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

    def gradient_descent(self, inputs, outputs):
        norm = Normalisation()
        self.split_data(inputs, outputs)

        xx = []
        xx_test = []
        for i in range(len(self.trainInputs[0])):
            xx.append([self.trainInputs[j][i] for j in range(len(self.trainInputs))])
        for i in range(len(self.testInputs[0])):
            xx_test.append([self.testInputs[j][i] for j in range(len(self.testInputs))])

        xx, xx_test = norm.tool_normalisation(xx, xx_test)

        newTrainInputs, newTestInputs = norm.standardisation(self.trainInputs, self.testInputs)
        newTrainOutputs, newTestOutputs = norm.standardisation([self.trainOutputs], [self.testOutputs])
        self.trainOutputs
        # self.plotData(self.trainInputs, newTrainInputs)
        self.trainInputs = newTrainInputs
        self.testInputs = newTestInputs
        #newTrainOutputs = norm.standardisation([self.trainOutputs])[0]
        #self.testOutputs = norm.standardisation([self.testOutputs])[0]
        # self.plotData(self.trainOutputs, newTrainOutputs)
        #self.trainOutputs = newTrainOutputs
        regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=100)
        for _ in range(100):
              regressor.partial_fit(xx, self.trainOutputs)
        #regressor.fit(xx, self.trainOutputs)

        w0, w1 = regressor.intercept_[0], regressor.coef_[0]
        print('sklearn - the learnt model: f(x) = ', w0, ' + ', w1, ' * x1 + ' , ' * x2')

        bgd = BatchGD(self.alpha, self.noEpochs)
        bgd.fit(self.trainInputs, self.trainOutputs)
        bgdComputed = bgd.predict(self.testInputs)
        print("batch manual : " + str(bgd.intercept) + " + x1 * " + str(bgd.coefs[0]) )

        # sgd = SGD(self.alpha, self.noEpochs)
        # sgd.fit(self.trainInputs, self.trainOutputs)
        # sgdComputed = sgd.predict(self.testInputs)
        # print("sgd manual : " + str(sgd.intercept) + " + x1 * " + str(sgd.coefs[0]) + " + x2 * " + str(sgd.coefs[1]))

        print("tool error bgd: " + str(mean_squared_error(self.testOutputs, bgdComputed)))
        #print("tool error sgd: " + str(mean_squared_error(self.testOutputs, sgdComputed)))
        print("manual error bgd: " + str(self.calculate_error(self.testOutputs, bgdComputed)))
        #print("manual error sgd: " + str(self.calculate_error(self.testOutputs, sgdComputed)))

        # self.plot_solution(bgd.intercept, bgd.coefs[0], bgd.coefs[1])


    def plotData(self, x, new_x):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        ax1.hist(x, 20)
        ax1.set_title('before normalisation')
        ax2.hist(new_x, 20)
        ax2.set_title('after normalisation')
        plt.show()

    def calculate_error(self, real, computed):
        error = 0
        for t1, t2 in zip(computed, real):
            error += (t1 - t2) ** 2
        return error / len(real)

    def plot3Ddata(self, x1Train, x2Train, yTrain, x1Model=None, x2Model=None, yModel=None, x1Test=None, x2Test=None,
                   yTest=None, title=None):

        ax = plt.axes(projection='3d')
        if (x1Train):
            plt.scatter(x1Train, x2Train, yTrain, c='r', marker='o', label='train data')
        if (x1Model):
            plt.scatter(x1Model, x2Model, yModel, c='b', marker='_', label='learnt model')
        if (x1Test):
            plt.scatter(x1Test, x2Test, yTest, c='g', marker='^', label='test data')
        plt.title(title)
        ax.set_xlabel("capita")
        ax.set_ylabel("freedom")
        ax.set_zlabel("happiness")
        plt.legend()
        plt.show()


    def plot_solution(self, w0, w1, w2):
        noOfPoints = 50
        xref1 = []
        val = min(self.trainInputs[0])
        step1 = (max(self.trainInputs[0]) - min(self.trainInputs[0])) / noOfPoints
        for _ in range(1, noOfPoints):
            for _ in range(1, noOfPoints):
                xref1.append(val)
            val += step1

        xref2 = []
        val = min(self.trainInputs[1])
        step2 = (max(self.trainInputs[1]) - min(self.trainInputs[1])) / noOfPoints
        for _ in range(1, noOfPoints):
            aux = val
            for _ in range(1, noOfPoints):
                xref2.append(aux)
                aux += step2

        yref = [w0 + w1 * el1 + w2 * el2 for el1, el2 in zip(xref1, xref2)]
        self.plot3Ddata(self.trainInputs[0], self.trainInputs[1], self.trainOutputs, xref1, xref2, yref, [], [], [], 'train data and the learnt model')

