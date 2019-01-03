# Considérons que vous avez à votre disposition un fichier texte contenant des phrases de différentes longueurs. 
# Écrivez un script qui recherche et affiche la phrase la plus longue.

import os

fileObj = open("testfile", "r")

lengthMax, longestLine = 0, ""
while 1:
    newLine = fileObj.readline()
    if newLine == "":
        break
    elif len(newLine) > lengthMax:
        lengthMax = len(newLine)
        longestLine = newLine

print(longestLine)