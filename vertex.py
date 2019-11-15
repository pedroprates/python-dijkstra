class Vertex:
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    @property
    def name(self):
        return self.__name
    
    @property
    def cost(self):
        return self.__cost

    def update_cost(self, value):
        self.__cost = value

    def __lt__(self, a):
        return self.cost() < a.cost()

    def __gt__(self, a):
        return self.cost() > a.cost()

    def __eq__(self, a):
        return self.cost() == a.cost()