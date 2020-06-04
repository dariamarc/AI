import random
import numpy as np

class myKMeans:
    def __init__(self, no_iter):
        self.no_iter = no_iter
        self.centroids = []

    def fit(self, inputs, no_clusters):
        self.centroids = [[] for _ in range(no_clusters)]

        randomSample = random.sample(range(len(inputs)), no_clusters)
        for i in range(len(randomSample)):
            self.centroids[i] = inputs[randomSample[i]]

        for iter in range(self.no_iter):
            results = [[] for _ in range(no_clusters)]

            for input in inputs:
                distances = [np.linalg.norm(input - self.centroids[centroid]) for centroid in range(len(self.centroids))]
                classification = distances.index(min(distances))
                results[classification].append(input)

            for classif in range(len(results)):
                self.centroids[classif] = np.average(results[classif], axis=0)


    def predict(self, inputs):
        computed = []
        for input in inputs:
            distances = [np.linalg.norm(input - self.centroids[centroid]) for centroid in range(len(self.centroids))]
            classification = distances.index(min(distances))
            computed.append(classification)

        return computed



