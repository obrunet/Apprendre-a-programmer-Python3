# Ecrivez un script qui recopie en Utf-8 un fichier texte encodé à l'origine en Latin-1, 
# en veillant en outre à ce que chaque mot commence par une majuscule. 
# Le programme demandera les noms des fichiers à l'utilisateur. 
# Les opérations de lecture et d'écriture des fichiers auront lieu en mode texte ordinaire. 

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