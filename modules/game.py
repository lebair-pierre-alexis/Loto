from modules.player import Player
from modules.files import loadPlayers, loadCards

class   Game:
    def __init__(self) -> None:
        self.players = loadPlayers()
        loadCards(self.players)
        self.remainingPlayers = list(self.players.keys())
        self.mode = self.chooseMode()
        self.keepPlaying = True
        self.hasEnded = False
        self.numPlayed = []

    def checkWin(self) -> None:
        if self.mode == 1:
            for player in self.players:
                winCon = self.players[player].hasWon()
                if winCon != 0:
                    print("Bingo !! ", self.players[player].name, " a gagné avec le carton n°", winCon, " !")
                    self.hasEnded = True
        elif self.mode == 2:
            for player in self.remainingPlayers:
                if self.players[player].hasLost():
                    self.remainingPlayers.remove(player)
                    if len(self.remainingPlayers) == 0:
                        print(player, " a perdu ... Il ne reste plus aucun joueur dans la course. Quel dommage :'( !)")
                        self.hasEnded = True
                    else :
                        print(player, " a perdu ... Il aura sans doute plus de chance la prochaine fois ;)")

    def chooseMode(self) -> int:
        mode = input("Veuillez choisir le mode de jeu : 1.Loto Normale | 2.Loto du perdant : ")
        while mode != "1" and mode != "2":
            print("Le mode que vous avez rentré n'existe pas")
            mode = input("Veuillez choisir le mode de jeu : 1.Loto Normale | 2.Loto du perdant : ")
        return(int(mode))

    def resetPlayers(self) -> None:
        for player in self.players:
            self.players[player].resetMarks()

    def playAgain(self) -> None:
        rematch = input("Voullez vous refaire une partie ? 1.oui | 2.non : ")
        while rematch != "1" and rematch != "2":
            print("Veuillez donner une réponse valide")
            rematch = input("Voullez vous refaire une partie ? 1.oui | 2.non : ")
        rematch = int(rematch)
        if rematch == 1:
            self.resetPlayers()
            self.mode = self.chooseMode()
            self.hasEnded = False
            self.numPlayed.clear()
        else:
            self.keepPlaying = False

    def stats(self) -> None:
        for player in self.players:
            self.players[player].showStat()

    def mark(self, number) -> None:
        for player in self.players:
            self.players[player].markCards(number, self.mode)
