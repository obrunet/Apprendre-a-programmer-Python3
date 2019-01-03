# Tâchez d’écrire une petite fonction trouve() qui fera exactement le contraire de ce que
# fait l’opérateur d’indexage (c’est-à-dire les crochets [ ]). Au lieu de partir d’un index
# donné pour retrouver le caractère correspondant, cette fonction devra retrouver l’in-
# dex correspondant à un caractère donné.
# En d’autres termes, il s’agit d’écrire une fonction qui attend deux arguments : le nom
# de la chaîne à traiter et le caractère à trouver. La fonction doit fournir en retour l’in-
# dex du premier caractère de ce type dans la chaîne. Ainsi par exemple, l’instruction :
# print(trouve("Juliette & Roméo", "&"))
# devra afficher : 9


def findChar (strName : str, char):
    i, j = 0, -1                                    # by default, return j = -1 if not found
    while i < len (strName):
        if strName[i] == char:
            j = i
            break
        i += 1
    return (j)


def main():
    choosenStr = input("Please enter a sentence:")
    choosenChar = input("Then enter a character:")
    index = findChar (choosenStr, choosenChar[0])
    if index == -1:
        print("This specific character cannot be found in the sentence.")
    else :
        print("This specific character has been found in the sentence, at index: ", index)


if __name__ == "__main__":
    main()