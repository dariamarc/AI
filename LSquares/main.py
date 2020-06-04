from repo.reader import Reader
import matplotlib.pyplot as plt
from service.least_squares import LeastSquaresMethod


def plotDataHistogram(x, variableName):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()

def main():
    reader = Reader("2017.csv")
    inputs1, inputs2, outputs = reader.read("Economy..GDP.per.Capita.", "Freedom", "Happiness.Score")
    # plotDataHistogram(inputs1, "GDP")
    # plotDataHistogram(inputs2, "Freedom")
    inputs = [inputs1, inputs2]
    plt.axes(projection="3d")
    plt.plot(inputs1, inputs2, outputs, 'ro')
    plt.xlabel('GDP capita')
    plt.ylabel('Freedom')
    plt.title('GDP capita, freedom vs. happiness')
    #plt.show()
    lsm = LeastSquaresMethod()
    lsm.least_squares_method(inputs, outputs)




main()