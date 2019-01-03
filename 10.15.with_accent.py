# Modifiez le script précédent pour explorer les codes situés entre 128 et 256, 
# où vous retrouverez nos caractères accentués (parmi de nombreux autres). 
# La relation numérique trouvée dans l’exercice précédent reste-t-elle valable aussi pour les caractères accentués du Français ? 

i = 128
while i <= 256:
    print("#", i, ":", chr(i), end=" / ")
    i += 1

# 192 : À -> 221 : Ý
# 224 : à -> 253 : ý
# lowercase = uppercase + 36 (not 32)