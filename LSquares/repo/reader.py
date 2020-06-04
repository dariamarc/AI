import csv


class Reader:
    def __init__(self, filename):
        self.__filename = filename

    def read(self, inputVariable1, inputVariable2, outputVariable):
        data = []
        dataNames = []
        with open(self.__filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    dataNames = row
                else:
                    data.append(row)
                line_count += 1
        selectedVariable1 = dataNames.index(inputVariable1)
        inputs1 = [float(data[i][selectedVariable1]) for i in range(len(data))]

        selectedVariable2 = dataNames.index(inputVariable2)
        inputs2 = [float(data[i][selectedVariable2]) for i in range(len(data))]
        selectedOutput = dataNames.index(outputVariable)
        outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

        return inputs1, inputs2, outputs
