# Compte le nombre d'occurences du caractère "e" dans une une chaine

str = "efffffffeffffffffffeffffffffffe"

i, c = 0, 0
while i< len(str):
    if str[i] == "e":                               
        c = c+1
    i=i+1
print("The string has", c, "caracter(s) 'e'")