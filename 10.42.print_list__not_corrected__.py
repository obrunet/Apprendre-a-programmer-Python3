# Écrivez une fonction imprime_liste() qui permette d’afficher ligne par ligne tous les éléments contenus dans une liste 
# de taille quelconque. Le nom de la liste sera fourni en argument. 
# Utilisez cette fonction pour imprimer la liste de nombres aléatoires générés par la fonction list_aleat(). 
# Ainsi par exemple, l’instruction imprime_liste(liste_aleat(8)) devra afficher une colonne de 8 nombres réels aléatoires. 

from random import *

def list_aleat(n):
    s = [0]*n
    for i in range(n):
        s[i] = random()
    return s

def print_list_col(list):
    for i in list:
        print(i)

if __name__ == "__main__":
    print_list_col(list_aleat(8))

