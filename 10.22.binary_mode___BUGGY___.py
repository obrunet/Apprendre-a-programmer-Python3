# Variante de l’exercice précédent : effectuez les opérations de lecture et d’écriture des 
# fichiers en mode binaire, et les opérations de décodage/encodage sur les séquences d’octets. 
# Au passage, vous traiterez les lignes de manière à remplacer tous les espaces par le groupe de 3 caractères « -*- ». 

import os

inputFile = input("Enter a source file name (Latin-1): ")
inFileObj = open(inputFile, "rb")                                           # b for binary mode

ouputFile = input("Enter a destination file name (Utf-8): ")                # b for binary mode
ouFileObj = open(ouputFile, "wb")

while 1:
    newLine = inFileObj.readline()
    if newLine == b"":
        break   
    tempStr = newLine.decode("Latin1")
    tempStr = tempStr.replace(" ","_*_")
    newLine = tempStr.encode("Utf-8")

inFileObj.close()
ouFileObj.close()