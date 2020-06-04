import csv
import os

import PIL
from PIL import Image
import numpy as np
from joblib.numpy_pickle_utils import xrange


class Reader:
    def readEmoji(self):
        inputs = []
        for i in range(1, 51):
            image = Image.open("emoji_grey/happy" + str(i) + ".png.jpg").resize((30, 30))
            data = np.asarray(image)
            inputs.append(data)

        for i in range(1, 51):
            image = Image.open("emoji_grey/sad" + str(i) + ".png.jpg").resize((30, 30))
            data = np.asarray(image)
            inputs.append(data)

        outputs = [[1, 0] for _ in range(50)] + [[0, 1] for _ in range(50)]

        return inputs, outputs

    def readFaces(self):
        inputs = []
        filenames = os.listdir('happy')
        lenHappy = len(filenames)
        for i in range(len(filenames)):
            image = Image.open("happy/" + filenames[i]).resize((48, 48))
            data = np.asarray(image)
            inputs.append(data)

        filenames = os.listdir('sadness')
        lenSad = len(filenames)
        for i in range(len(filenames)):
            image = Image.open("sadness/" + filenames[i]).resize((48, 48))
            data = np.asarray(image)
            inputs.append(data)

        outputs = [[1, 0] for _ in range(lenHappy)] + [[0, 1] for _ in range(lenSad)]

        return inputs, outputs
