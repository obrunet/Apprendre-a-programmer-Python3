"""
# Ecrire un programme destiné à vérifier le fonctionnement du générateur de nombres aléatoires de Python en appliquant la théorie exposée ci-dessus. 
# Votre programme devra donc : 
# • Demander à l’utilisateur le nombre de valeurs à tirer au hasard à l’aide de la fonction random(). 
#   Il serait intéressant que le programme propose un nombre par défaut (1000 par exemple). 
# • Demander à l’utilisateur en combien de fractions il souhaite partager l’intervalle des valeurs possibles (c’est-à-dire l’intervalle de 0 à 1). 
#   Ici aussi, il faudrait proposer un nombre de fractions par défaut (5 par exemple). 
#   Vous pouvez également limiter le choix de l’utilisateur à un nombre compris entre 2 et le 1/10e du nombre de valeurs tirées au hasard. 
# • Construire une liste de N compteurs (N étant le nombre de fractions souhaitées). Chacun d’eux sera évidemment initialisé à zéro. 
# • Tirer au hasard toutes les valeurs demandées, à l’aide de la fonction random() , et mémoriser ces valeurs dans une liste. 
# • Mettre en œuvre un parcours de la liste des valeurs tirées au hasard (boucle), et effectuer un test sur chacune d’elles 
#   pour déterminer dans quelle fraction de l’intervalle 0-1 elle se situe. Incrémenter de une unité le compteur correspondant. 
# • Lorsque c’est terminé, afficher l’état de chacun des compteurs.
"""

from random import random

if __name__ == "__main__":
    user_answer = input("Enter a number of values to be randomly choosen by the random() func - 1 000 by default: ") 
    if user_answer == "":
        input_nb = 1000
    else:
        input_nb = int(user_answer)
        
    user_answer = input("In how many groups do you want to split up the nb of random values - 5 by default : ")
    if user_answer == "":
        group_nb = 5
    else:
        group_nb = int(user_answer)

    random_values = [random() for i in range(input_nb)]
    representative_list = [0] * group_nb

    i = 0
    group_min, group_max = 0, 1/group_nb
    while i < group_nb:
        for val in random_values:
            if (group_min < val) and (val < group_max):
                representative_list[i] += 1
        group_min, group_max = i/group_nb, (i+1)/group_nb
        i += 1

    print(representative_list)