# Variante de l’exercice précédent : effectuez les opérations de lecture et d’écriture des
# fichiers en mode binaire, et les opérations de décodage/encodage sur les séquences
# d’octets. Au passage, vous traiterez les lignes de manière à remplacer tous les espaces
# par le groupe de 3 caractères « -*- »            168

import os

inputFile = input("Enter a source file name (Latin-1): ")
inFileObj = open(inputFile, "r", encoding ="Latin-1")

ouputFile = input("Enter a destination file name (Utf-8): ")
ouFileObj = open(ouputFile, "w", encoding ="Utf8")

while 1:
    newLine = inFileObj.readline()
    if newLine == "":
        break
    else:
        newLine = newLine.title()
        ouFileObj.write(newLine)


inFileObj.close()
ouFileObj.close()