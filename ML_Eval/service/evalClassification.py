from math import log


def confusionMatrix(realLabels, computedLabels, labels):
    # elementele din matrice - confMat[i][j] = elementul de la indicii i si j face parte din clasa
    # i dar a fost plasat in clasa j
    confMat = [[0 for i in range(len(labels))] for j in range(len(labels))]
    for i in range(len(computedLabels)):
        idx_actual = idx_predicted = 0
        for j in range(len(labels)):
            if realLabels[i] == labels[j]:
                idx_actual = j
            if computedLabels[i] == labels[j]:
                idx_predicted = j
        confMat[idx_actual][idx_predicted] += 1

    return confMat

def evalClassification(realLabels, computedLabels, labels):
    confMat = confusionMatrix(realLabels, computedLabels, labels)

    accuracy = sum(confMat[i][i] for i in range(len(labels))) / len(realLabels)

    precision = [0 for i in range(len(labels))]
    for i in range(len(labels)):
        positives = 0
        for j in range(len(labels)):
            positives += confMat[j][i]
        precision[i] = confMat[i][i] / positives

    recall = [0 for i in range(len(labels))]
    for i in range(len(labels)):
        positives = 0
        for j in range(len(labels)):
            positives += confMat[i][j]
        recall[i] = confMat[i][i] / positives

    return accuracy, precision, recall

def get_labels_from_prob(probs, labels):
    return [labels[i.index(max(i))] for i in probs]

def evalClassificationProb(realLabels, probabilities, labels):
    computedLabels = get_labels_from_prob(probabilities, labels)
    return evalClassification(realLabels, computedLabels, labels)

#cross entropy
def classificationLoss(realLabels, computedLabels, labels):
    loss = 0
    j = 0
    for i in computedLabels:
        loss += log(computedLabels[j][labels.index(i)])
        j += 1
    return -loss / (len(realLabels))