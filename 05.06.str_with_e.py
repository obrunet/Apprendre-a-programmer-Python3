# Détermine si une chaine contient ou non lecaractère "e"

str = "Dans la forêt lointaine on entend le hibou..."

i=0
while i< len(str):
    if str[i] == "e":                               
        print("The string has a 'e' at position", i+1)
        break
    elif i == len(str):
        print("The string doesn't have any 'e'")
    i=i+1

