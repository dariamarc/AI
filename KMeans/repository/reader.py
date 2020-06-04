import csv


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
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

        inputs = [data[i][0] for i in range(len(data))]
        outputs = [data[i][1] for i in range(len(data))]
        labelNames = list(set(outputs))

        return inputs, outputs, labelNames