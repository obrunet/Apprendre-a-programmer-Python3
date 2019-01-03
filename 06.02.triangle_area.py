# Écrivez un programme qui calcule le périmètre et l’aire d’un triangle quelconque 
# dont l’utilisateur fournit les 3 côtés. 

from math import sqrt

print("Enter the 3 sides of a triangle (separeted by a comma):")

l = list(eval(input()))
a = l[0]
b = l[1]
c = l[2]


perimeter = a+b+c
d = perimeter/2
area = sqrt(d*(d-a)*(d-b)*(d-c))
del d

print("The perimeter is equal to", perimeter, "\nThe area is esqual to", area)