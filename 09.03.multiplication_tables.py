# Écrivez un script qui génère automatiquement un fichier texte contenant les tables de multiplication de 2 à 30 
# (chacune d’entre elles incluant 20 termes seulement). 

import os

fileObj = open("multiplicationTables.txt", "w+")

for i in range (2,31):
    for j in range (1,21):
         fileObj.write(str(i*j))
         fileObj.write("  ")
         j = j+1
    fileObj.write("\n")
    i = i+1

fileObj.close()


# verification
fileObj = open("multiplicationTables.txt", "r")
for i in range (2,31):
    print(fileObj.readline())
    i = i+1
