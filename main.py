from Card import Card
from Minion import Minion

def main():

    deck=[]

    acornBearer = Minion('Acorn Bearer', 1, 2, 1)
    deck.append(acornBearer)
    crystalPower = Card('Crystal Power', 1)
    deck.append(crystalPower)
    razorBoar = Minion('Razor Boar', 2, 2, 2)
    deck.append(razorBoar)
    vileCall = Card('Vile Call', 3)
    deck.append(vileCall)

    
    for card in deck:
        card.printCard()
        print('\n')


if __name__ == "__main__":
    main()