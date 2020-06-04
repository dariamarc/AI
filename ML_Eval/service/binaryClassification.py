from math import log

# cross entropy
def binaryClassificationLoss(realLabels, probs, labels):
    loss = 0
    for i in range(len(realLabels)):
        idx = labels[realLabels[i]]
        if (idx == 1):
            loss += log(probs[i][idx])
        else:
            loss += log(1 - probs[i][idx])
    return -loss