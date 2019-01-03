# Écrivez un script qui permette de créer et de relire aisément un fichier texte. 
# Votre programme demandera d’abord à l’utilisateur d’entrer le nom du fichier. 
# Ensuite il lui proposera le choix, soit d’enregistrer de nouvelles lignes de texte, soit d’afficher le contenu du fichier. 
# L’utilisateur devra pouvoir entrer ses lignes de texte successives en utilisant simplement la touche <Enter> 
# pour les séparer les unes des autres. Pour terminer les entrées, il lui suffira d’entrer une ligne vide 
# (c’est-à-dire utiliser la touche <Enter> seule). 
# L’affichage du contenu devra montrer les lignes du fichier séparées les unes des autres de la manière la plus naturelle 
# (les codes de fin de ligne ne doivent pas apparaître).


import os               #from os import open


fileName = input("Enter the file's name:")
answerNb = int(input("Do you want to add new lines in the textfile ? -> [1]\nDo you want to read the content of the textfile ? -> [2]\n"))


def writeFile():
    fileObj = open(fileName, 'a')
    while 1:
        newLine = input("Enter a new line to add:")
        if newLine == "":
            break
        else:
            fileObj.write(newLine + '\n')
    fileObj.close()


def readFile():
    fileObj = open(fileName, 'r')
    while 1:
        rLine = fileObj.readline()
        if rLine == "":
            break
        else:
            print(rLine)
    fileObj.close()


if answerNb == 1:
    writeFile()
elif answerNb == 2:
    readFile()
else:
    print("Your choice is different than 1 or 2 -> exit.")