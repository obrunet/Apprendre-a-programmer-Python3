# Créez une liste A contenant quelques éléments. Effectuez une vraie copie de cette liste
# dans une nouvelle variable B. Suggestion : créez d’abord une liste B de même taille que
# A mais ne contenant que des zéros. Remplacez ensuite tous ces zéros par les éléments
# tirés de A.

random_list = list (range(73, -20, -7))
print(random_list)
cpy_list = [0] * len(random_list)
#print(cpy_list, len(random_list), len(cpy_list))

i = 0
while i < len(random_list):
    cpy_list[i:i+1] = [random_list[i]] # pourquoi quand on met cpy_list[i:i] le programme copie toutes la liste de 0 à nouveau à la fin ??
    i += 1
print(cpy_list)