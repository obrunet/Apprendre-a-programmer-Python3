# Réécrivez la fonction list_aleat() ci-dessous, en utilisant la méthode append() pour construire la liste petit à petit à partir 
# d’une liste vide (au lieu de remplacer les zéros d’une liste préexistante comme nous l’avons fait). 

from random import *

def list_aleat(n):
    s = [0]*n
    for i in range(n):
        s[i] = random()
    return s

def list_append(n):
    s = []
    for i in range(n):
        s.append(random())
    return s

if __name__ == "__main__":
    print(list_aleat(6))
    print(list_aleat(6))
    print(list_aleat(6))
    print(list_append(6))
    print(list_append(6))
    print(list_append(6))
