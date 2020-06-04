from heapq import heapify

from GA import GA
from Reader import Reader

# functia de fitness are ca argumente permutarea si matricea de adiacenta
#calculeaza valoarea drumului care trece prin toate orasele dat de permutare
def roadValue(nodes, matrix):
    value = 0
    index = 0
    while index < len(nodes) - 1:
        value += matrix[nodes[index]][nodes[index + 1]]
        index += 1

    value += matrix[nodes[len(nodes) - 1]][nodes[0]]
    return value


def main():
    reader = Reader()
    reader._init_("mediumF.txt")
    net = reader.readNetwork()

    gaParam = {"popSize": 500, "noGen": 500}
    problParam = {'function': roadValue, 'noNodes': net['noNodes'], 'net': net['mat']}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    stop = False
    g = -1
    solutions = []

    while not stop and g < gaParam['noGen']:
        g += 1
        ga.oneGenerationElitism()
        bestChromo = ga.bestChromosome()
        solutions.append(bestChromo)
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(
            bestChromo.fitness))

    heapify(solutions)
    print(str(solutions[0]))

main()