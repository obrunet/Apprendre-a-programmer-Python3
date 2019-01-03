# Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. 
# Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], 
# ce programme devrait afficher : le plus grand élément de cette liste a la valeur 75

l = [32, 5, 12, 8, 3, 75, 2, 15]
greatestElt = 0

i=0
while i < len(l):
    if l[i]> greatestElt:
        greatestElt = l[i]
    i = i+1
print("The greastest element of the list is", greatestElt)