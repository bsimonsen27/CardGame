#child class of Card
from Card import Card

class Minion(Card):
    def __init__(self, name, cost, attackPoints, health):
        Card.__init__(self, name, cost)
        self.attackPoints = attackPoints
        self.health = health

    def printCard(self):
        Card.printCard(self)
        print('Attack Points:', self.attackPoints)
        print('Health Points:', self.health)