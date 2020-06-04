class Edge:
    def __init__(self, a, b, weigth):
        self.__source = a
        self.__dest = b
        self.__weigth = weigth
        self.__pheromone = 0.5

    @property
    def source(self):
        return self.__source

    @property
    def dest(self):
        return self.__dest

    @property
    def weigth(self):
        return self.__weigth

    @property
    def pheromone(self):
        return self.__pheromone

    @pheromone.setter
    def pheromone(self, x):
        self.__pheromone = x

    def __str__(self):
        return "Source " + str(self.source) + " Destination " + str(self.dest) + " Weigth " + str(self.weigth) + " Pheromone " + str(self.pheromone)
