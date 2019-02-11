# Définissez une classe JeuDeCartes() permettant d’instancier des objets dont le comportement soit similaire à celui d’un vrai jeu de cartes. La classe devra comporter au moins les quatre méthodes suivantes : 
#  • méthode constructeur : 
    # création et remplissage d’une liste de 52 éléments, qui sont eux-mêmes des tuples de 2 entiers. 
    # Cette liste de tuples contiendra les caractéristiques de chacune des 52 cartes. 
    # Pour chacune d’elles, il faut en effet mémoriser séparément un entier indiquant la valeur (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
    # les 4 dernières valeurs étant celles des valet, dame, roi et as), et un autre entier indiquant la couleur de la carte (c’est-à-dire 3,2,1,0 pour Cœur, Carreau, Trèfle et Pique). Dans une telle liste, 
    # l’élément (11,2) désigne donc le valet de Trèfle, et la liste terminée doit être du type : [(2, 0), (3,0), (3,0), (4,0), ..... (12,3), (13,3), (14,3)] 
# • méthode nom_carte() : cette méthode doit renvoyer, sous la forme d’une chaîne, l’identité d’une carte quelconque dont 
    # on lui a fourni le tuple descripteur en argument. Par exemple, l’instruction : print(jeu.nom_carte((14, 3))) doit provoquer l’affichage de : As de pique 
# • méthode battre() : comme chacun sait, battre les cartes consiste à les mélanger. Cette méthode sert donc à mélanger les éléments de la liste contenant les cartes, quel qu’en soit le nombre. 
# • méthode tirer() : lorsque cette méthode est invoquée, une carte est retirée du jeu. Le tuple contenant sa valeur et sa couleur est renvoyé 
    # au programme appelant. On retire toujours la première carte de la liste. Si cette méthode est invoquée alors qu’il ne reste plus aucune carte dans la liste, 
    # il faut alors renvoyer l’objet spécial None au programme appelant. 

import random

class Cardgame(object):
    "Definition of the Cardgame class with the following methods: constructor, card_name, shuffle, choose_card, choose_card_randomly"

    def __init__(self):
        "Creates a list of 52 tuples, each tuples represent a card of the game (height & color)"
        self.card_game = []
        for i in range(2,15):
            for j in range(0,4):
                self.card_game.append((i,j))
                j += 1
            i += 1
    
    def card_name(self, card):
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

    def choose_card_randomly(self):
        "Chooses randomly a card of the game & returns it, DOESN'T delete it, if no card left returns 'none' "
        if len(self.card_game) == 0:
            return None
        return self.card_game[(random.randint(0, 51))]

    def shuffle(self):
        "Randomize the game even if there is alreday some cards left/chosen, if no card left returns 'none'"
        l = len(self.card_game)     
        if l == 0:
            return None
        for i in range (9):     # i = nb of times the game is shuffled
            self.card_game = random.sample(self.card_game, k = l)


if __name__ == "__main__":
    cg = Cardgame()

    # prints a randomly chosen card
    cr = cg.choose_card_randomly()
    print("A randomly chosen card: ", cg.card_name(cr), "\n")

    # randomizes the game
    if cg.shuffle() == None:
        print("No card in the game...")

    # displays all the cards 
    for n in range(53):
        c = cg.choose_card()
        if c == None:
            print("End of the game!")
        else:
            print(cg.card_name(c))
        n += 1