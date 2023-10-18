from modules.card import Card

class   Player:

    def __init__(self, name) -> None:
        self.name = name
        self.cards: dict[int, Card] = {}

    def hasWon(self) -> int:
        for card in self.cards:
            winCard = self.cards[card].isFull()
            if winCard != 0:
                return winCard
        return 0

    def hasLost(self) -> bool:
        for card in self.cards:
            if self.cards[card].isEmpty() == True:
                return False
        return True

    def resetMarks(self) -> None:
        for card in self.cards:
            self.cards[card].resetMark()

    def showStat(self) -> None:
        print("--------------------------------------- ", self.name, " ---------------------------------------")
        lowest = 15
        cardNums = []
        for card in self.cards:
            if self.cards[card].remaining < lowest:
                lowest = self.cards[card].remaining
                cardNums.clear()
                cardNums.append(self.cards[card].number)
            elif self.cards[card].remaining == lowest:
                cardNums.append(self.cards[card].number)
        print("Le ou les cartons les plus avancés de sont :")
        for cardNum in cardNums:
            print("Carton n°", cardNum, " avec ", lowest, " nombre(s) manquant(s) :")
            print(self.cards[cardNum].missingNumbers())
        print("------------------------------------------------------------------------------------------")

    def markCards(self, number, mode) -> None:
        print("--------------------------------------- ", self.name, " ---------------------------------------")
        foundCards = []
        remainingCards = 0
        for card in self.cards:
            if self.cards[card].hasNum(number):
                foundCards.append(card)
                self.cards[card].markNum(number)
            else:
                remainingCards += 1
        if mode == 1:
            print("Nombre de carton ayant le nombre ", number, " : ", len(foundCards))
            if len(foundCards) != 0:
                print("Cartons :")
                for cardNum in foundCards:
                    print(" - n°", cardNum)
        else:
            print(len(foundCards), " cartons éliminés !")
            if len(foundCards) != 0:
                for cardNum in foundCards:
                    print(" - n°", cardNum)
            print(remainingCards, " cartons restants")
        print("------------------------------------------------------------------------------------------")
