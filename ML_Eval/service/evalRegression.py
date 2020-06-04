from math import sqrt

# de asemenea si loss
def evalRegressionMAE(realOutputs, computedOutputs):
    error = 0
    for i in range(len(realOutputs)):
        for j in range(len(realOutputs[i])):
            error += abs(realOutputs[i][j] - computedOutputs[i][j])

    return error / len(realOutputs)

def evalRegressionRMSE(realOutputs, computedOutputs):
    error = 0
    for i in range(len(realOutputs)):
        for j in range(len(realOutputs[i])):
            error += pow((realOutputs[i][j] - computedOutputs[i][j]), 2)

    return sqrt(error / len(realOutputs))