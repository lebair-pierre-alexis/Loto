from os import listdir
from player import Player

def loadPlayers() -> dict[Player]:
    playersName = listdir("players/")
    for name in playersName:
        name.replace(".txt", "")
