from Card import Card
from Minion import Minion

def main():

    deck=[]

    cards = open("Cards.txt", 'r')
    
    for card in cards:
        cardInfo = card.split(',')
        nameOfCard = cardInfo[0]
        costOfCard = cardInfo[1]

        lengthOfList = len(cardInfo)

        if lengthOfList == 2:
            cardData = Card(nameOfCard, costOfCard)

        if lengthOfList == 4:
            attackP = cardInfo[2]
            healthP = cardInfo[3]
            cardData = Minion(nameOfCard, costOfCard, attackP, healthP)
        
        deck.append(cardData)


    cards.close()

    
    for card in deck:
        card.printCard()
        print('\n')


if __name__ == "__main__":
    main()