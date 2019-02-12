# Complément de l’exercice précédent : définir deux joueurs A et B. Instancier deux jeux de cartes (un pour chaque joueur) et les mélanger. 
# Ensuite, à l’aide d’une boucle, tirer 52 fois une carte de chacun des deux jeux et comparer leurs valeurs. 
# Si c’est la première des deux qui a la valeur la plus élevée, on ajoute un point au joueur A. 
# Si la situation contraire se présente, on ajoute un point au joueur B. Si les deux valeurs sont égales, on passe au tirage suivant. 
# Au terme de la boucle, comparer les comptes de A et B pour déterminer le gagnant.

import random

class Cardgame(object):
    "Definition of the Cardgame class with the following methods: constructor, display_card, shuffle, choose_card, choose_card_randomly"

    def __init__(self):
        "Creates a list of 52 tuples, each tuples represent a card of the game (height & color)"
        self.card_game = []
        for i in range(2,15):
            for j in range(0,4):
                self.card_game.append((i,j))
                j += 1
            i += 1
    
    def display_card(self, card):
        "Receive a tuple descriptor (for instance (14, 3)) & displays the card name: its heigth and color ('Ace of Spades' here)"
        name_dict = {11: 'Jack', 12:'Lady', 13:'King', 14:'Ace'}
        name = name_dict.get(card[0], card[0])
        color_dict = {0: 'Spades', 1: 'Clover', 2:'Diamond', 3:'Heart'}
        color = color_dict.get(card[1], card[1])
        return("This card is a {} of {}".format(name, color))

    def choose_card(self):
        "Chooses & returns the 1st card of the game, then deletes it, if no card left returns 'none' "
        if len(self.card_game) == 0:
            return None
        card = self.card_game[0]
        self.card_game.remove(card)
        return card

    def shuffle(self):
        "Randomize the game even if there is alreday some cards left/chosen, if no card left returns 'none'"
        l = len(self.card_game)     
        if l == 0:
            return None
        for i in range (9):     # i = nb of times the game is shuffled
            self.card_game = random.sample(self.card_game, k = l)


if __name__ == "__main__":
    # creates 2 games, one for each player, and shuffle the games
    game_a, game_b = Cardgame(), Cardgame()
    game_a.shuffle()
    game_b.shuffle()

    # match between the 2 players
    pt_a, pt_b = 0, 0
    for i in range(52):
        card_a, card_b = game_a.choose_card(), game_b.choose_card()
        if  card_a[0] > card_b[0]:
            pt_a += 1
        elif card_a[0] < card_b[0]:
            pt_b += 1
        i += 1

    # who's the winner ?
    if pt_a > pt_b:
        print("And the winner is... player A! Congratz :)")
    elif pt_a < pt_b:
        print("And the winner is... player B! Congratz :)")
    else:
        print("Equality! ... no winner :)")