# Demander à l’utilisateur qu’il entre un nombre. 
# Afficher ensuite : soit la racine carrée de ce nombre, 
# soit un message indiquant que la racine carrée de ce nombre ne peut être calculée.

from math import sqrt

print("Enter a floating number", end=" ")
nb=float(input())

if nb<0:
    print("The square root of a negative number cannot be calculated!")
else:
    print("The square root of this number is equal to ", sqrt(nb))