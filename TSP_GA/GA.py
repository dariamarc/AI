from random import randint

from Chromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param["popSize"]):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres, self.__problParam['net'])

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def selection(self):
        # best = randint(0, self.__param["popSize"] - 1)
        #
        # for i in range(self.__param['noElite'] - 1):
        #     pos = randint(0, self.__param["popSize"] - 1)
        #     if self.__population[pos].fitness < self.__population[best].fitness:
        #         best = pos
        # return best
        pos1 = randint(0, self.__param["popSize"] - 1)
        pos2 = randint(0, self.__param["popSize"] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param["popSize"]):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        oldPop = self.__population
        newPop = [self.bestChromosome()]
        for _ in range(self.__param["popSize"] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)

        # pastrez jumatatea cea mai buna din generatia veche si jumatatea cea mai buna din generatia de copii
        pop = []
        oldPop.sort()
        newPop.sort()
        for i in range(self.__param['popSize']):
            pop.append(oldPop[i])
            pop.append(newPop[i])
        self.__population = pop
        self.evaluation()


    def oneGenerationSteadyState(self):
        for _ in range(self.__param["popSize"]):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres, self.__problParam['net'])
            worst = self.worstChromosome()
            if (off.fitness < worst.fitness):
                worst = off