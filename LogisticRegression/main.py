from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

from service.logistic import LR


def plotDataHistogram(x, variableName):
    n, bins, patches = plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()

def main():
    data = load_iris()
    inputs = data['data']
    outputs = data['target']
    outputNames = data['target_names']
    featureNames = list(data['feature_names'])
    feature1 = [feat[featureNames.index('sepal length (cm)')] for feat in inputs]
    feature2 = [feat[featureNames.index('sepal width (cm)')] for feat in inputs]
    feature3 = [feat[featureNames.index('petal length (cm)')] for feat in inputs]
    feature4 = [feat[featureNames.index('petal width (cm)')] for feat in inputs]
    # inputs = [[feat1, feat2, feat3, feat4], [feat1, feat2, feat3, feat4], ...]
    inputs = [[feat[featureNames.index('sepal length (cm)')], feat[featureNames.index('sepal width (cm)')], feat[featureNames.index('petal length (cm)')], feat[featureNames.index('petal width (cm)')]] for feat in inputs]
    # plotDataHistogram(feature1, "sepal length")
    # plotDataHistogram(feature2, "sepal width")
    # plotDataHistogram(feature3, "petal length")
    # plotDataHistogram(feature4, "petal width")
    # plotDataHistogram(outputs, "iris class")

    features = [feature1, feature2, feature3, feature4]
    lr = LR()
    lr.lr(inputs, outputs, features, outputNames)

main()