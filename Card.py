# class is a blueprint of an Object
class Card:
    #attributes
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    #behaviors 
    def printCard(self):
        print ("Name:", self.name)
        print ("Cost:", self.cost)