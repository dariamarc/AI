import csv


class Reader:
    def __init__(self):
        self.filename = 'data/posts.csv'

    def readData(self):
        data = []
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    dataNames = row
                else:
                    data.append(row)
                line_count += 1

        inputs = [[data[i][0], data[i][1]] for i in range(len(data))]
        outputs = [data[i][4] for i in range(len(data))]
        imageOutputs = [data[i][2] for i in range(len(data))]
        textOutputs = [data[i][3] for i in range(len(data))]
        return inputs, outputs, imageOutputs, textOutputs