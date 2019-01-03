# Écrivez un script qui compare les contenus de deux fichiers et signale la première différence rencontrée

import os

fileName1, fileName2 = input("Enter the name of the file number 1:"), input("Enter the name of the file number 2:")
fileObject1, fileObject2 = open(fileName1, 'r'), open(fileName2, 'r')

carIndex, flag = 1, 1       # flag = 1 by default the two files are identical

while 1:
    file1Car, file2Car = fileObject1.read(1), fileObject2.read(1)
    if file1Car == file2Car:
        carIndex = carIndex+1
    else:
        flag = 0
        print("The the character", carIndex, "differs in the two files.")
        break

if flag == 1:
    print("The two files are the same")