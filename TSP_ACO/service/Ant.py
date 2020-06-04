from random import uniform, random

from service.Utils import findEdge


class Ant:
    def __init__(self, startNode, problParam = None):
        self.__problParam = problParam  # noNodes, edges - lista cu muchiile, feromon, parametrul q0, alpha, beta
        self.__path = [startNode]
        self.__distance = 0

    @property
    def path(self):
        return self.__path

    @property
    def distance(self):
        return self.__distance


    def select_node(self):
        not_visited = [node for node in range(1, self.__problParam['noNodes'] + 1) if node not in self.__path]
        current_node = self.__path[-1]
        q = uniform(0, 1)
        if q > self.__problParam['q0']:
            best = 0
            best_node = not_visited[0]
            for node in not_visited:
                w = self.__problParam['mat'][current_node - 1][node - 1]
                ph = self.__problParam['phMat'][current_node - 1][node - 1]
                d = 1/w
                selection = pow(ph, self.__problParam['alpha']) * pow(d, self.__problParam['beta'])
                if selection > best:
                    best = selection
                    best_node = node
            return best_node

        else:
            best = 0
            best_node = not_visited[0]
            node_to_return = None
            prob = uniform(0,1)
            nominator = 0.0
            for node in not_visited:
                w = self.__problParam['mat'][current_node - 1][node - 1]
                ph = self.__problParam['phMat'][current_node - 1][node - 1]
                d = 1 / w
                selection = pow(ph, self.__problParam['alpha']) * pow(d, self.__problParam['beta'])
                nominator = nominator + selection

            for node in not_visited:
                w = self.__problParam['mat'][current_node - 1][node - 1]
                ph = self.__problParam['phMat'][current_node - 1][node - 1]
                d = 1/w
                selection = pow(ph, self.__problParam['alpha']) * pow(d, self.__problParam['beta'])
                if selection / nominator > prob:
                    node_to_return =  node
                if selection / nominator > best:
                    best = selection / nominator
                    best_node = node

            if node_to_return != None:
                return node_to_return
            else:
                return best_node


    def update_pheromone(self, node1, node2):
        self.__problParam['phMat'][node1 - 1][node2 - 1]  =  self.__problParam['phMat'][node1 - 1][node2 - 1] * (1 - self.__problParam['phDecay'])
        self.__problParam['phMat'][node1 - 1][node2 - 1] += self.__problParam['phDecay'] * self.__problParam['pheromone']
        self.__problParam['phMat'][node2 - 1][node1 - 1] = self.__problParam['phMat'][node1 - 1][node2 - 1]


    def add_node_to_path(self):
        self.__path.append(self.select_node())
        self.__distance = self.__distance + self.__problParam['mat'][self.__path[-2] - 1][self.__path[-1] - 1]

        # daca se ajunge la ultimul nod se ia in considerare si distanta de intoarcere la primul nod
        if len(self.__path) == self.__problParam['noNodes']:
            last_node = self.__path[-1]
            first_node = self.__path[0]
            self.__distance = self.__distance + self.__problParam['mat'][last_node - 1][first_node - 1]

    def find_path(self):
        while len(self.path) < self.__problParam['noNodes']:
            self.add_node_to_path()

        for node_idx in range(1,len(self.path)):
            self.update_pheromone(self.path[node_idx], self.path[node_idx - 1])
        self.update_pheromone(self.path[-1], self.path[0])

    def calculate_distance(self):
        self.__distance = 0
        for i in range(1, len(self.__path)):
            self.__distance +=  self.__problParam['mat'][self.__path[i] - 1][self.__path[i - 1] - 1]

        self.__distance += self.__problParam['mat'][self.__path[-1] - 1][self.__path[0] - 1]