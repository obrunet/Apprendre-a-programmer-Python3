# Écrivez un script qui tire au hasard des cartes à jouer. Le nom de la carte tirée doit être correctement présenté, « en clair ». 
# Le programme affichera par exemple : 
# Frappez <Enter> pour tirer une carte : Dix de Trèfle 
# Frappez <Enter> pour tirer une carte : As de Carreau 
# Frappez <Enter> pour tirer une carte : Huit de Pique 
# Frappez <Enter> pour tirer une carte : etc.

from random import randrange

while True:
    user_answer = input("Please press <Enter> to randomly chose a card - Press 'q' to exit:")
    if user_answer == 'q':
        break
    else:
        height = randrange(13)          # ace, 2 3 4 5 6 7 8 9 10, jack, lady, king -> 13
        height += 1                     # because randrange returns a value between 0 and 12
        if height == 1:
            height = "Ace"
        elif height == 13:
            height = "King"
        elif height == 12:
            height = "Lady" 
        elif height == 11:
            height = "Jack"

        color = randrange(4)
        color = "of heart" if (color == 0) else color
        color = "of spades" if (color == 1) else color
        color = "of diamonds" if (color == 2) else color
        color = "of clover" if (color == 3) else color

        print(height, color)