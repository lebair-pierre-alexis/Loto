from modules.card import Card
from modules.player import Player
from modules import files

if __name__ == "__main__":
    players = files.loadPlayers()
    files.loadCards(players)
