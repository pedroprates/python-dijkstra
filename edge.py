class Edge:
    def __init__(self, source, destination, cost):
        self.__source = source
        self.__destination = destination
        self.__cost = cost

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def cost(self):
        return self.__cost
