from repo.reader import Reader
from service.classifyPosts import computeLabels
from service.predictPosts import MyPredictor


def main():
    reader = Reader()
    inputs, outputs, imageOutputs, textOutputs = reader.readData()
    predictor = MyPredictor()
    predictor.predict(inputs, outputs, imageOutputs, textOutputs)

main()