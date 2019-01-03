# Définissez une fonction indexMax(liste) qui renvoie l’index de l’élément ayant la valeur la plus élevée dans 
# la liste transmise en argument. 
# Exemple d’utilisation : serie = [5, 8, 2, 1, 9, 3, 6, 7] 
# print(indexMax(serie)) 4

def indexMax (serie):
    i, indexMax, maxi = 0, 0, 0
    while i < len(serie):
        if serie[i] > maxi:
            maxi, indexMax = serie[i], i
        i = i+1
    return(indexMax)

serie = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(serie))