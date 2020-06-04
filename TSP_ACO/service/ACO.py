import math
from random import randint, uniform
from service.Ant import Ant


class ACO:
    def __init__(self, problParam, param):
        self.__problParam = problParam # noNodes, mat - matricea de adiacenta, feromon, parametrul q0, alpha, beta, coef de evap
        self.__param = param # noSteps, colonySize
        self.__colony = []
        self.__bestPath = []
        self.__bestDistance = math.inf


    def initialize_colony(self):
        colony = []
        for i in range(self.__param['colonySize']):
            start_node = randint(1, self.__problParam['noNodes'])
            ant = Ant(start_node, self.__problParam)
            colony.append(ant)
        return colony


    def update_pheromone_for_best(self, path, distance):
        delta = 1 / distance
        node_idx = 0
        while node_idx < len(path) - 1:
            node1 = path[node_idx]
            node2 = path[node_idx + 1]
            self.__problParam['phMat'][node1 - 1][node2 - 1] = (1 - self.__problParam['phEvap']) * self.__problParam['phMat'][node1 - 1][node2 - 1] + self.__problParam['phEvap'] * delta
            self.__problParam['phMat'][node2 - 1][node1 - 1] = self.__problParam['phMat'][node1 - 1][node2 - 1]

            node_idx = node_idx + 1
        self.__problParam['phMat'][path[-1] - 1][path[0] - 1] = (1 - self.__problParam['phEvap']) * \
                                                           self.__problParam['phMat'][path[-1] - 1][path[0] - 1] + \
                                                           self.__problParam['phEvap'] * delta

        self.__problParam['phMat'][path[0] - 1][path[-1] - 1] = self.__problParam['phMat'][path[-1] - 1][path[0] - 1]

    # def update_pheromone(self):
    #     newPhMat = [[0 for i in range(self.__problParam['noNodes'])] for j in range(self.__problParam['noNodes'])]
    #     for ant in self.__colony:
    #         for node in range(1, len(ant.path)):
    #             newPhMat[node - 2][node - 1] += self.__problParam['pheromone'] / ant.distance
    #             newPhMat[node - 1][node - 2] += self.__problParam['pheromone'] / ant.distance
    #         newPhMat[ant.path[-1] - 1][ant.path[0] - 1] += self.__problParam['pheromone'] / ant.distance
    #         newPhMat[ant.path[0] - 1][ant.path[-1] - 1] += self.__problParam['pheromone'] / ant.distance
    #
    #     idx_row = 0
    #     for row in self.__problParam['phMat']:
    #         idx_col = 0
    #         for el in row:
    #             self.__problParam['phMat'][idx_row][idx_col] *= (1 - self.__problParam['phEvap'])
    #             self.__problParam['phMat'][idx_col][idx_row] *= (1 - self.__problParam['phEvap'])
    #             self.__problParam['phMat'][idx_row][idx_col] += newPhMat[idx_row][idx_col]
    #             self.__problParam['phMat'][idx_col][idx_row] += newPhMat[idx_col][idx_row]
    #             idx_col += 1
    #         idx_row += 1

    def aco(self):
        for idx in range(self.__param['noSteps']):
            print()
            self.__colony = self.initialize_colony()
            best_ant = self.__colony[0]

            # fiecare furnica isi gaseste drumul
            for ant in self.__colony:
                ant.find_path()
                if best_ant.distance > ant.distance:
                    best_ant = ant

            # la fiecare iteratie furnica cea mai buna intareste urma de feromon
            self.update_pheromone_for_best(best_ant.path, best_ant.distance)

            print("Best solution at step " + str(idx) + ": "+ str(best_ant.path) + " " + str(best_ant.distance))

            # se actualizeaza cea mai buna solutie obtinuta din iteratii
            if best_ant.distance < self.__bestDistance:
                self.__bestDistance = best_ant.distance
                self.__bestPath = best_ant.path

        print("Best solution is: " + str(self.__bestPath) + " with distance = " + str(self.__bestDistance))

    def aco_dynamic(self):
        # modifica lungimile din graf pe parcursul algoritmului
        for idx in range(self.__param['noSteps']):
            self.__colony = self.initialize_colony()
            best_ant = self.__colony[0]

            # fiecare furnica isi gaseste drumul
            for ant in self.__colony:
                ant.find_path()
                if best_ant.distance > ant.distance:
                    best_ant = ant

            # modificarea grafului
            if idx % (self.__param['noSteps'] // 5) == 0 and idx > 0:
                # se modifica lungimile din graf
                self.modify_graph()

                # se recalculeaza distanta pentru cel mai bun drum gasit pana acum
                self.calculate_distance()

                # se modifica lungimea path-ului pentru fiecare furnica
                for ant in self.__colony:
                    ant.calculate_distance()
                    if best_ant.distance > ant.distance:
                        best_ant = ant
            # se intareste urma de feromon pe cel mai bun drum gasit
            self.update_pheromone_for_best(best_ant.path, best_ant.distance)

            print("Best solution at step " + str(idx) + ": "+ str(best_ant.path) + " " + str(best_ant.distance))
            # se actualizeaza cea mai buna solutie obtinuta din iteratii
            if best_ant.distance < self.__bestDistance:
                self.__bestDistance = best_ant.distance
                self.__bestPath = best_ant.path

        print("Best solution is: " + str(self.__bestPath) + " with distance = " + str(self.__bestDistance))

    def modify_graph(self):
        for i in range(len(self.__problParam['mat'])):
            for j in range(len(self.__problParam['mat'][i])):
                p = uniform(0.1, 0.8);
                self.__problParam['mat'][i][j] += p;

    def calculate_distance(self):
        self.__bestDistance = 0
        for i in range(1, len(self.__bestPath)):
            self.__bestDistance += self.__problParam['mat'][self.__bestPath[i] - 1][self.__bestPath[i - 1] - 1]

        self.__bestDistance += self.__problParam['mat'][self.__bestPath[-1] - 1][self.__bestPath[0] - 1]
