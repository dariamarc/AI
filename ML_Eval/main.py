import sklearn

from service.binaryClassification import binaryClassificationLoss
from service.evalClassification import evalClassification, evalClassificationProb, classificationLoss
from service.evalRegression import evalRegressionMAE, evalRegressionRMSE
from sklearn.metrics import mean_absolute_error, accuracy_score, precision_score, recall_score


def main():
    print("Multi-target regression evaluation:")
    realOutputs = [[1, 5, 2], [7, 4, 2], [1, 6, 5], [2, 3, 9]]
    computedOutputs = [[1, 5, 2], [7.3, 4, 2.1], [0.9, 5.8, 5], [2, 3, 9]]
    print("MAE:   " + str(evalRegressionMAE(realOutputs, computedOutputs)))
    print("RMSE:  " + str(evalRegressionRMSE(realOutputs, computedOutputs)) + '\n')

    print("Multi-class classification evaluation: ")
    realLabels = ['dog', 'cat', 'cat', 'panda', 'dog', 'panda', 'cat', 'panda', 'dog']
    computedLabels = ['dog', 'cat', 'dog', 'cat', 'dog', 'panda', 'cat', 'cat', 'dog']
    labels = ['dog', 'cat', 'panda']
    acc_eval, prec_eval, recall_eval = evalClassification(realLabels, computedLabels, labels)
    print("Manual evaluation: acc = " + str(acc_eval) + " prec = " + str(prec_eval) + " recall = " + str(recall_eval))
    acc_tool = accuracy_score(realLabels, computedLabels)
    precision_tool = precision_score(realLabels, computedLabels, average=None, labels=labels)
    recall_tool = recall_score(realLabels, computedLabels, average=None, labels=labels)
    print("sklearn: acc = " + str(acc_tool) + " prec = " + str(precision_tool) + " recall = " + str(recall_tool) + '\n')

    print("Multi-class classification with probabilities:")
    realLabels = ['dog', 'cat', 'cat', 'panda', 'dog', 'panda', 'cat', 'panda', 'dog']
    probs = [[0.7, 0.2, 0.1], [0.3, 0.6, 0.1], [0.5, 0.4, 0.1], [0.2, 0.5, 0.3], [0.6, 0.2, 0.2],
             [0.2, 0.2, 0.6], [0.2, 0.7, 0.1], [0.1, 0.5, 0.4], [0.6, 0.2, 0.2]]
    acc_eval, prec_eval, recall_eval = evalClassificationProb(realLabels, probs, labels)
    print("Manual evaluation: acc = " + str(acc_eval) + " prec = " + str(prec_eval) + " recall = " + str(recall_eval))
    print("Loss = " + str(classificationLoss(realLabels, probs, labels)) + '\n')

    print("Binary classification loss:")
    real = ['spam', 'ham', 'spam', 'spam', 'ham', 'ham', 'ham', 'spam']
    proba = [[0.6, 0.4], [0.2, 0.8], [0.4, 0.6], [0.7, 0.3], [0.3, 0.7], [0.6, 0.4], [0.6, 0.4], [0.7, 0.3]]
    labelNames = {'spam' : 1, 'ham' : 0}
    print("Loss = " + str(binaryClassificationLoss(real, proba, labelNames)))

main()