# Demander à l’utilisateur d’entrer trois longueurs a, b, c. 
# À l’aide de ces trois longueurs, déterminer s’il est possible de construire un triangle. 
# Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque. 
# Attention : un triangle rectangle peut être isocèle.

print("Enter the 3 sides of a triangle (separated by a float):", end=" ")
a, b, c = eval(input())

# Can a triangle be made with these sides ?
if a<(b+c) and b<(c+a) and c<(a+b):
    print("A triangle can be made with these sides.")

    test=0
    if a==b and b==c :
        test=1
        print("This is an equilateral triangle")
    elif a==b or b==c or c==a :
        test=1
        print("This is an isosceles triangle")
    if a*a == b*b+c*c or b*b == c*c+a*a or c*c == a*a+b*b :
        test=1
        print("This is a rectangular triangle")
    if test==0:
        print("This is not a particular triangle...")

else:
    print("A triangle can NOT be made with these sides.")

