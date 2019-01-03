# Écrivez un programme qui calcule la période d’un pendule simple de longueur donnée. 
# La formule qui permet de calculer la période d’un pendule simple est T=2 pi racine (l/g), 
# l représentant la longueur du pendule et g la valeur de l’accélération de la pesanteur au lieu d’expérience. 

from math import sqrt

g = 9.81
pi = 3.14159

print("Enter the pendulum's length")
l = int(input())

T=2*pi*sqrt(l/g)
print("The pendulum's period is equal to", T, ".s") 