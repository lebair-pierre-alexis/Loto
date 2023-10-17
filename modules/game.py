from player import Player

class   Game:
    def __init__(self, players :dict[str, Player]) -> None:
        self.players = players
        self.remainingPlayers = list(players.keys())
        self.mode = 1
        pass

    def checkWin(self) -> bool:
        if self.mode == 1:
            for player in self.players:
                winCon = player.hasWon()
                if winCon != 0:
                    print("Bingo !! ", player.name, " a gagné avec le carton n°", winCon, " !")
                    return True
            return False
        elif self.mode == 0:
            for player in self.remainingPlayers:
                if self.players[player].hasLost():
                    self.remainingPlayers.remove(player)
                    if len(self.remainingPlayers) == 0:
                        print(player, " a perdu ... Il ne reste plus aucun joueur dans la course. Quel dommage :'( !)")
                        return True
                    print(player, " a perdu ... Il aura sans doute plus de chance la prochaine fois ;)")
            return False
