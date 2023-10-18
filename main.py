from modules.card import Card
from modules.player import Player
from modules.game import Game

if __name__ == "__main__":
    print("Bienvenue dans l'outil ultime du Loto game !")
    game = Game()
    while game.keepPlaying:
        print("Début de la partie !")
        print("Rappel des commandes textuelles :")
        print(" - [1-99] : Entrer un nombre entre 1 et 99 permet de valider les cases correspondantes pour tous les joueurs sur tous leurs cartons")
        print(" - stats : Permet d'avoir un recap donnant pour chaque joueur le nombre de cartons les plus proches de la victoire, leur numéro, leurs numéros manquants")
        while game.hasEnded == False:
            cmd = input("Entrez une commande : ")
            if cmd == "stats":
                game.stats()
            elif cmd == "win":
                print("Félicitation ", game.remainingPlayers[0], " est le dernier survivant et gagne la partie !")
                game.hasEnded = True
            elif cmd == "quit":
                game.hasEnded = True
            elif cmd.isdigit() and int(cmd) >= 1 and int(cmd) <= 99:
                cmd = int(cmd)
                if cmd in game.numPlayed:
                    print("Ce nombre à déjà été joué")
                else:
                    game.numPlayed.append(cmd)
                    game.mark(cmd)
                    game.checkWin()
            else:
                print("Commande invalide")
                print(" - [1-99] : Entrer un nombre entre 1 et 99 permet de valider les cases correspondantes pour tous les joueurs sur tous leurs cartons")
                print(" - stats : Permet d'avoir un recap donnant pour chaque joueur le nombre de cartons les plus proches de la victoire, leur numéro, leurs numéros manquants")
        game.playAgain()
    print("Merci d'avoir joué !")
