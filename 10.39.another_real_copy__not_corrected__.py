# Même question, autre suggestion encore : pour créer la liste B, découpez dans la liste A
# une tranche incluant tous les éléments (à l’aide de l’opérateur [:]).


random_list = list (range(73, -20, -7))
print(random_list)
cpy_list = []

cpy_list[:] = random_list[:]                # copy the whole list
print(cpy_list)

cpy_list[-1:0] = random_list[-3:]           # replace last elt by the last third elts
print(cpy_list)

cpy_list[-1] = random_list[-3:]             # replace last elt by a list
print(cpy_list)