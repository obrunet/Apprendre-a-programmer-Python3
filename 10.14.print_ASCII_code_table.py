# Écrivez un petit script qui affiche une table des codes ASCII. 
# Le programme doit afficher tous les caractères en regard des codes correspondants. 
# À partir de cette table, établissez la relation numérique simple reliant chaque 
# caractère majuscule au caractère minuscule correspondant.

i = 32                                      # printable symbols start from 32
while i <= 127:
    print("#", i, ":", chr(i), end=" / ")
    i += 1

# 65 : A 
# 97 : a 
# lowercase = uppercase + 32