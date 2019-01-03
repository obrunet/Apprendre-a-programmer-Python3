# Écrivez un programme qui permette d’encoder des valeurs dans une liste. 
# Ce programme devrait fonctionner en boucle, l’utilisateur étant invité à entrer sans cesse de nouvelles valeurs, 
# jusqu’à ce qu’il décide de terminer en frappant <Enter> en guise d’entrée. 
# Le programme se terminerait alors par l’affichage de la liste. 
# 
# Exemple de fonctionnement :
# Veuillez entrer une valeur : 25 
# Veuillez entrer une valeur : 18 
# Veuillez entrer une valeur : 6284 
# Veuillez entrer une valeur : 
# [25, 18, 6284]

l, i = [], 1

while i != "":
    print("Enter a value:", end=" ")
    i = input()
    if i != "":
        i = int(i)
        l.append(i)
print(l)