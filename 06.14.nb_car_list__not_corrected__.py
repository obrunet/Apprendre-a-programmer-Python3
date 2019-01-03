# Soit la liste suivante : 
# ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise'] 
# Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant. 

l1 = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
l2 = []             # need to be declared to be used in the while loop

i=0
while i < len(l1):
    l2.append(l1[i])
    l2.append(len(l1[i]))
    i = i+1
print(l2)