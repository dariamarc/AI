import math
from heapq import heappush, _heapify_max
from queue import Queue


'''Pe loc'''
def distance(xA, yA, xB, yB):
    res = math.sqrt((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB))
    return res


def distanceTest():
    assert math.fabs(distance(1, 5, 4, 1) - 5.0) < math.pow(10, -3)
    assert math.fabs(distance(1, 1, 1, 1) - 0) < math.pow(10, -3)
    assert math.fabs(distance(-8, -4.5, 17, 6.5) - 27.313) < math.pow(10, -3)


#O(n * log n)
def last(s):
    lista = list(s.split(' '))
    lista.sort()
    return lista[len(lista) - 1]


def lastTest():
    assert last("Ana are mere rosii si galbene") == "si"
    assert last("") == ""
    assert last("7 7 3 2") == "7"
    assert last("am fugit , pa") == "pa"



'''Acasa'''
#1
#O(n)
def duplicate(lista):
    n = len(lista)
    suma = n * (n - 1) / 2
    sumList = sum(lista)

    return int(sumList - suma)


#2
def duplicate2(lista):
    frecv = [0] * len(lista)
    for i in lista:
        if frecv[i] > 0:
            return i
        frecv[i] = frecv[i] + 1



def duplicateTest():
    assert duplicate([1, 2, 3, 4, 2]) == 2
    assert duplicate([1, 2, 3, 4, 3, 5]) == 3
    assert duplicate([1, 2, 3, 4, 5, 5]) == 5
    assert duplicate2([1, 2, 3, 4, 2]) == 2
    assert duplicate2([1, 2, 3, 4, 3, 5]) == 3
    assert duplicate2([1, 2, 3, 4, 5, 5]) == 5


#3
#O(n logn)
def kthelement2(lista, k):
    if k > len(lista):
        return -1

    lista.sort(reverse=True)
    return lista[k - 1]


#4
#O(n)
def kthelement(lista, k):
    if k > len(lista):
        return -1
    else:
        heap = []
        for i in lista:
            heappush(heap, i)

        _heapify_max(heap)
        return heap[k - 1]


def kthelementTest():
    assert kthelement([1, 3, 2, 6, 5, 4], 3) == 4
    assert kthelement([1, 2, 3], 5) == -1
    assert kthelement([7, 4, 6, 3, 9, 1], 2) == 7
    assert kthelement2([1, 3, 2, 6, 5, 4], 3) == 4
    assert kthelement2([1, 2, 3], 5) == -1
    assert kthelement2([7, 4, 6, 3, 9, 1], 2) == 7


#5
def binary(n):
    q = Queue()

    q.put("1")
    res = []

    while(n > 0):
        n = n - 1
        s1 = q.get()
        res.append(s1)
        s2 = s1
        q.put(s1 + "0")
        q.put(s2 + "1")

    return res


#6
def binary2(n):
    lista = []
    j = 0
    for i in range(1, n + 1):
        b = bin(i)[2:] #pune si prefixul 0b la inceput
        lista.append(b)
    return lista


def binaryTest():
    assert binary(10) == ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']
    assert binary(2) == ['1', '10']
    assert binary(3) == ['1', '10', '11']
    assert binary(4) == ['1', '10', '11', '100']
    assert binary2(10) == ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']
    assert binary2(2) == ['1', '10']
    assert binary2(3) == ['1', '10', '11']
    assert binary2(4) == ['1', '10', '11', '100']


#7
def scalar(a, b):
    s = 0
    for i in range(0, len(a)):
        s = s + a[i] * b[i]
    return s


def scalarTest():
    a = [1, 0, 2, 0, 3]
    b = [1, 2, 0, 3, 1]
    assert scalar(a, b) == 4
    a = []
    b = []
    assert scalar(a, b) == 0


#8
def matrixSum(matrix, x1, y1, x2, y2):
    suma = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            suma += matrix[i][j]
    return suma


def matrixSumTest():
    m = [[0, 2, 5, 4, 1],
         [4, 8, 2, 3, 7],
         [6, 3, 4, 6, 2],
         [7, 3, 1, 8, 3],
         [1, 5, 7, 9, 4]]
    assert matrixSum(m, 1, 1, 3, 3) == 38
    m = []
    assert matrixSum(m, 1, 11, 1, 1) == 0


#9
def binaryMatrix(matrix):
    n = len(matrix)
    if n == 0:
        return -1

    m = len(matrix[0])
    maxim = 0
    for i in range(n):
        suma = 0
        for j in range(m):
            suma += matrix[i][j]
        if suma > maxim:
            maxim = suma
            line = i

    return line


def binaryMatrixTest():
    m = [[0, 0, 1, 1, 1],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 1, 1]]
    assert binaryMatrix(m) == 0
    m = [[0, 0, 1, 1, 1],
         [0, 1, 1, 0, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
    assert binaryMatrix(m) == 2
    m = []
    assert binaryMatrix(m) == -1


#10
def major(lista):
    if len(lista) == 0:
        return False

    fr = [0] * 100
    for i in range(len(lista)):
        fr[lista[i]] += 1

    maxim = -1
    for i in range(100):
        if fr[i] > maxim:
            maxim = fr[i]
            nr = i

    if maxim > len(lista) / 2:
        return nr

    return False


def majorTest():
    assert major([2, 2, 3, 4, 2, 4, 2, 5]) == False
    assert major([3, 7, 8, 3, 3, 3, 3, 3, 3]) == 3
    assert major([13, 13, 13, 13]) == 13
    assert major([]) == False


def main():
    distanceTest()
    lastTest()
    duplicateTest()
    kthelementTest()
    binaryTest()
    scalarTest()
    matrixSumTest()
    binaryMatrixTest()
    majorTest()


main()
