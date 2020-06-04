import numpy as np
from repo.reader import Reader
from service.dataOps import flatten, split_data, normalisation, shuffle
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

from service.myANN import NeuralNetwork


def emojiPredict():
    reader = Reader()
    inputs, outputs = reader.readEmoji()
    inputs, outputs = shuffle(inputs, outputs)
    trainInputs, testInputs, trainOutputs, testOutputs = split_data(inputs, outputs)
    # normalisedTrain, normalisedTest = normalisation(trainInputs, testInputs)
    trainInputs = np.array(trainInputs)
    trainOutputs = np.array(trainOutputs)
    testInputs = np.array(testInputs)
    testOutputs = np.array(testOutputs)

    print('Keras emoji............')
    model = Sequential()

    model.add(Conv2D(32, kernel_size=5, activation='relu', input_shape=(30, 30, 3)))
    model.add(Conv2D(32, kernel_size=5, activation='relu'))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Flatten())
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(trainInputs, trainOutputs, validation_data=(testInputs, testOutputs), epochs=20)

    trainInputs = trainInputs.tolist()
    trainOutputs = trainOutputs.tolist()
    testInputs = testInputs.tolist()
    testOutputs = testOutputs.tolist()
    simpleOutputs_train = []
    for i in trainOutputs:
        if i[0] == 1:
            simpleOutputs_train.append(1)
        else:
            simpleOutputs_train.append(0)
    simpleOutputs_test = []
    for i in testOutputs:
        if i[0] == 1:
            simpleOutputs_test.append(1)
        else:
            simpleOutputs_test.append(0)

    trainInputs = flatten(trainInputs)
    testInputs = flatten(testInputs)
    normalisedTrain, normalisedTest = normalisation(trainInputs, testInputs)

    print('My ANN emoji....................')
    net = NeuralNetwork(1, 4, 20)
    net.fit(normalisedTrain, simpleOutputs_train, 0.01)
    computed = net.predict(normalisedTest)

    error = 0.0
    for t1, t2 in zip(computed, simpleOutputs_test):
        if (t1 != t2):
            error += 1

    print("Manual error: " + str(error / len(trainInputs)))