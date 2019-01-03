# À partir de deux fichiers préexistants A et B, construisez un fichier C qui contienne 
# alternativement un élément de A, un élément de B, un élément de A... et ainsi de suite 
# jusqu’à atteindre la fin de l’un des deux fichiers originaux. 
# Complétez ensuite C avec les éléments restant sur l’autre. 

import os

fileNameA, fileNameB = input("Enter the name of the 1st file:"), input("Enter the name of the 2nd file:")
fileObjectA, fileObjectB = open(fileNameA,'r'), open(fileNameB, 'r')

fileObjectC = open(fileNameA + fileNameB, 'w')

while 1:
    fileCarA, fileCarB = fileObjectA.read(1), fileObjectB.read(1)
    if fileCarA == "" and fileCarB != "":
        while fileCarB != "":
            fileObjectC.write(fileCarB)
            fileCarB = fileObjectB.read(1)
            break
    elif fileCarA != "" and fileCarB == "":
        while fileCarA != "":
            fileObjectC.write(fileCarA)
            fileCarA = fileObjectA.read(1)
            break
    elif fileCarA == "" and fileCarB == "":
        break
    else:
        fileObjectC.write(fileCarA)
        fileObjectC.write(fileCarB)

fileObjectA.close()
fileObjectB.close()
fileObjectC.close()


# verification : print the file C = mix file A + B
fileObjectC = open(fileNameA + fileNameB, 'r')
while 1:
    newLine = fileObjectC.readline()
    if newLine != "":
        print(newLine)
    else:
        break
fileObjectC.close()
