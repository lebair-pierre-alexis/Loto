from os import listdir
from modules.player import Player
from modules.card import Card

def loadCards(players: dict[str, Player]) -> None:
    for player in players:
        file = open("players/" + player + ".txt", 'r')
        line = file.readline()
        while line:
            line = line.split(':')
            cardNum = int(line[0])
            players[player].cards[cardNum] = Card(cardNum)
            numbers = line[1].split(',')
            for number in numbers:
                players[player].cards[cardNum].numbers[int(number)] = 0
            line = file.readline()
    file.close()


def loadPlayers() -> dict[str, Player]:
    playerFiles = listdir("players/")
    players: dict[str, Player] = {}
    for playerName in playerFiles:
        playerName = playerName.replace(".txt", "")
        players[playerName] = Player(playerName)
    loadCards(players)
    return players
