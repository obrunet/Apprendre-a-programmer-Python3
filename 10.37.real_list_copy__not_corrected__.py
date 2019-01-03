# Même question, mais autre suggestion : créez d’abord une liste B vide. Remplissez-la
# ensuite à l’aide des éléments de A ajoutés l’un après l’autre.


random_list = list (range(73, -20, -7))
print(random_list)
cpy_list = []

for elt in random_list:
    cpy_list.append(elt) 

print(cpy_list)