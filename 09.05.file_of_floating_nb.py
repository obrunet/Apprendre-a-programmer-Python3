# Vous avez à votre disposition un fichier texte dont chaque ligne est 
# la représentation d’une valeur numérique de type réel (mais sans exposants). 
# Par exemple : 
# 14.896 
# 7894.6 
# 123.278 etc. 
# Écrivez un script qui recopie ces valeurs dans un autre fichier 
# en les arrondissant en nombres entiers (l’arrondi doit être correct)

import os

def roundNb (st):                   # input: a string
    nb = float(st) + 0.5            
    return (int(nb))

def makeCopy (fileNameSc, fileNameDest):
    fileObjectSc = open(fileNameSc,'r')
    fileObjectDest = open(fileNameDest, "w")
    while 1:
        newLine = fileObjectSc.readline()
        if newLine == "":
            break
        else:
            newLine = str(roundNb(newLine))+"\n"
            fileObjectDest.write(newLine)
    fileObjectSc.close()
    fileObjectDest.close()

def verification(st):
    fileObject = open(st,"r")
    while 1:
        newLine = fileObject.readline()
        if newLine == "":
            break
        else:
            print(newLine)

makeCopy("test", "testbak")
verification("testbak")
