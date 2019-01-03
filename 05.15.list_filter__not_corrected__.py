# Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots 
# (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) 
# pour générer deux nouvelles listes. 
# L’une contiendra les mots comportant moins de 6 caractères, l’autre les mots comportant 6 caractères ou davantage.

l = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra', "Maurice", "Louis", "Martin", "Léo"]
lLess, lMore = [], []

for i in range (0, len(l)):
    if len(l[i])<6:
        lLess.append(l[i])
    else:
        lMore.append(l[i])
    i = i+1
print(lLess)
print(lMore)