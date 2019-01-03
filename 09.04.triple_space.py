# Écrivez un script qui recopie un fichier texte en triplant tous les espaces entre les mots.

#teststr = "triple the spaces of a line."

import os

fileName = input("Enter file's name:")

def tripleSpaceOfaLine (st):
    i, retStr = 0, ""
    while i < len (st):
        if st[i] == " ":
            retStr = retStr + "   "
        else:
            retStr = retStr + st[i]
        i = i+1
    return retStr

def main():
    fileObject = open(fileName, 'r+')                   # r+ for read/write mode

    # all lines are put in a list
    allLinesList = fileObject.readlines()

    # for each string of the list, triple spaces
    for i in range(0,len(allLinesList)):
        allLinesList[i] = tripleSpaceOfaLine(allLinesList[i])
        i = i+1

    fileObject.seek(0)                  # position at the beginning
    fileObject.writelines(allLinesList)
    fileObject.close()


def verification():
    fileObject = open(fileName,"r")
    while 1:
        newLine = fileObject.readline()
        if newLine == "":
            break
        else:
            print(newLine)

if __name__ == "__main__":
    main()
    verification()
