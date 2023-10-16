from card import Card

class   Player:

    def __init__(self, name) -> None:
        self.name = name
        self.cards: list[Card] = []
        pass

    def addCard(self) -> None:
        number = int(input("Veuillez entrez le numéro du carton : "))
        card = Card(number)
        while card.remaining != 15:
            num = int(input("Nombre n°", card.remaining + 1, " : "))
            if card.asNum(num):
                print("Ce nombre à déjà été entré sur ce carton")
            else:
                card.numbers[num] = 0
                card.remaining += 1
        self.cards.append(card)

    def checkWin(self) -> bool:
        for card in self.cards:
            winCard = card.isFull()
            if winCard != 0:
                return winCard
        return False

    def checkLoss(self) -> bool:
        for card in self.cards:
            if card.isEmpty() == True:
                return False
        return True

    def resetMarks(self) -> None:
        for card in self.cards:
            card.resetMark()

    def showStat(self) -> None:
        lowest = 15
        cardNums = {}
        for card in self.cards:
            if card.remaining < lowest:
                lowest = card.remaining
                cardNums.clear()
                cardNums[card.number]
            elif card.remaining == lowest:
                cardNums.append(card.number)
        print("Le ou les cartons les plus avancés de ", self.name, " sont :")
        for cardNum in cardNums:
            print("Carton n°", cardNum, " avec ", lowest, " nombre(s) manquant(s) :")
            print(self.cards[cardNum].missingNumbers())
