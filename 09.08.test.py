# Écrivez un script qui permette d’encoder un fichier texte dont les lignes contiendront chacune 
# les noms, prénom, adresse, code postal et no de téléphone de différentes personnes 
# (considérez par exemple qu’il s’agit des membres d’un club). 

import os


def retrieveClubMemberInfo ():
    memberName = input("Enter the surname of the club's member:")
    memberFirstName = input("Enter the firstname of the club's member:")
    memberPostalCode = input("Enter the postal code of the club's member:")
    memberPhoneNb = input("Enter the phone number of the club's member:")
    return([memberName, memberFirstName, memberPostalCode, memberPhoneNb])


def saveInfo (textfile, memberInfo):
    # a -> append the file each time
    fileObject = open(textfile, "a")

    # enter the member's infos in 1 line
    for i in range (0, len(memberInfo)):
        fileObject.write(memberInfo[i]+" ")
        i += 1
    
    # next line -> for a new member's info
    fileObject.write("\n")
    fileObject.close()


def main ():
    answer, mBdatabase = "y", "memberdb.txt"
    while answer == "y":
        answer = str(input("Would you like to add the infos of a new member in the database ? [y] or [n]: "))
        if answer != "y":
            break
        else:
            saveInfo(mBdatabase, retrieveClubMemberInfo())


if __name__ == "__main__":
    main()


