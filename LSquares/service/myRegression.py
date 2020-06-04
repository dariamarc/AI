import numpy as np

class bivariateRegression:
    def __init__(self):
        self.intercept = 0.0
        self.coef_ = []

    def transpose(self, matrix):
        result = []
        for j in range(len(matrix[0])):
            result.append([])
            for i in range(len(matrix)):
                result[j].append(matrix[i][j])
        return result

    def multiplication(self, matrix1, matrix2):
        if (isinstance(matrix2[0], list)):
            result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += matrix1[i][k] * matrix2[k][j]
            return result

        result = []
        for i in range(len(matrix1)):
            sum = 0
            for j in range(len(matrix1[i])):
                sum += matrix1[i][j] * matrix2[j]
            result.append(sum)
        return result

    def minor(self, matrix, i, j):
        # i - randul, j = coloana
        result = []
        idx = -1
        for n in range(i):
            # pentru fiecare rand mai mic decat i se pun valorile de pe coloane fara coloana j
            idx += 1
            result.append([])
            for m in range(j):
                result[idx].append(matrix[n][m])
            for m in range(j + 1, len(matrix[0])):
                result[idx].append(matrix[n][m])
        for n in range(i + 1, len(matrix)):
            # pentru fiecare rand mai mare ca i se pun valorile de pe coloane fara coloana j
            idx += 1
            result.append([])
            for m in range(j):
                result[idx].append(matrix[n][m])
            for m in range(j + 1, len(matrix[0])):
                result[idx].append(matrix[n][m])
        return result

    def determinant(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * self.determinant(self.minor(matrix, 0, i))
        return det

    def inversion(self, matrix):
        determinant = self.determinant(matrix)
        if determinant != 0:
            adjunctMatrix = []
            for i in range(len(matrix)):
                cofactor = []
                for j in range(len(matrix)):
                    cofactor.append((-1) ** (i + j) * self.determinant(self.minor(matrix, i, j)))
                adjunctMatrix.append(cofactor)
            adjunctMatrix = self.transpose(adjunctMatrix)
            for i in range(len(adjunctMatrix)):
                for j in range(len(adjunctMatrix)):
                    adjunctMatrix[i][j] /= determinant
            return adjunctMatrix

    def fit(self, inputs, outputs):
        self.coef_ = [0.0 for i in range(len(inputs))]
        x = [[1, inputs[0][i], inputs[1][i]] for i in range(len(inputs[0]))]
        y = [[i] for i in outputs]
        x_trans = self.transpose(x)
        multi = self.multiplication(x_trans, x)
        # multi2 = np.linalg.inv(multi).dot(x_trans)
        multi2 = self.multiplication(self.inversion(multi), x_trans)
        result = self.multiplication(multi2, y)
        self.intercept = result[0][0]
        for i in range(len(self.coef_)):
            self.coef_[i] = result[i + 1][0]


    def eval(self, inputs, idx):
        # ia toate input-urile si indexul pentru care se calculeaza
        yi = self.intercept
        for j in range(len(inputs)):
            yi += self.coef_[j] * inputs[j][idx]
        return yi

    def predict(self, inputs):
        yComputed = []
        for i in range(len(inputs[0])):
            yComputed.append(self.eval(inputs, i))

        return yComputed

