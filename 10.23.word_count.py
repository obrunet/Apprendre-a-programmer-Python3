# Écrivez un script qui compte le nombre de mots contenus dans un fichier texte. 

import os

inFileObj = open("testLatin1.txt", "r", encoding="Latin-1")
n = 0

while 1:
    newLine = inFileObj.readline()
    if newLine == "":
        break
    n += len(newLine.split())

result = "The are {} words in this text file."
print(result.format(n))

inFileObj.close()