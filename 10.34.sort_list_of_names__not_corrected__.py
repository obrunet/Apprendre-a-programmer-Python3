# Vous avez à votre disposition un fichier texte qui contient un certain nombre de noms d’élèves. 
# Écrivez un script qui effectue une copie triée de ce fichier.

unsortedlist = ['Jean', 'Emmanuelle', 'Albert', 'Bertrand', 'Zain', 'Rachid', 'Jessica']
print(unsortedlist)
unsortedlist.sort()
print(unsortedlist)

# Other solution : case-insensitive sorting can use the lower() method BUT will work fine for ASCII-only contexts.

names = ['Jasmine', 'Alberto', 'Ross', 'dig-dog']
print ("The solution for this is about this names being sorted:", sorted(names, key=lambda name:name.lower()))