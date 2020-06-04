from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


def tool(trainInputs, testInputs, testOutputs, labels, no_clusters):
    unsupervisedClassifier = KMeans(n_clusters=no_clusters, max_iter=1000, random_state=0)
    unsupervisedClassifier.fit(trainInputs)
    computedTestIndexes = unsupervisedClassifier.predict(testInputs)
    computedTestOutputs = [labels[value] for value in computedTestIndexes]

    print(computedTestOutputs)
    print(testOutputs)
    print("Acc tool: ", accuracy_score(testOutputs, computedTestOutputs))