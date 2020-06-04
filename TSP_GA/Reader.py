from math import sqrt


class Reader:

    def _init_(self, filename):
        self.__filename = filename

    @staticmethod
    def _distance(a, b):
        return sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]))

    def readNetwork(self):
        network = {}
        if self.__filename == "berlin52.txt" or self.__filename == "hardE.txt":
            f = open(self.__filename, "r")
            text = f.read().split("\n")

            length = int(text[3].split(':')[1])
            network['noNodes'] = length
            f.readline()
            f.readline()
            lines = []
            for i in range(6, length + 6):
                line = text[i].split(" ")
                lines.append((float(line[1]), float(line[2])))
            mat = [[0.0 for i in range(length)] for i in range(length)]

            for i in range(0, length - 1):
                for j in range(i + 1, length):
                    mat[j][i] = mat[i][j] = self._distance(lines[i], lines[j])
            network['mat'] = mat

        else:
            f = open(self.__filename, "r")
            text = f.read()
            lines = text.split("\n")
            length = int(lines[0])
            network['noNodes'] = length
            mat = []
            for i in range(1, length + 1):
                line = lines[i].split(",")
                matrix = []
                for j in line:
                    matrix.append(int(j))
                mat.append(matrix)
            network['mat'] = mat

        return network