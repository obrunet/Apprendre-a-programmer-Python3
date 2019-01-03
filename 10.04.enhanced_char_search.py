# Améliorez la fonction de l’exercice précédent en lui ajoutant un troisième paramètre :
# l’index à partir duquel la recherche doit s’effectuer dans la chaîne. Ainsi par exemple,
# l’instruction :
# print(trouve ("César & Cléopâtre", "r", 5))
# devra afficher : 15 (et non 4 !).


def findChar (strName : str, char, beginIndex : int):
    i, j = 0, -1                                    # by default, return j = -1 if not found
    while i < len (strName):
        if i > beginIndex:
            if strName[i] == char:
                j = i
                break
        i += 1
    return (j)


def main():
    userStr = input("Please enter a sentence:")
    userChar = input("Then enter a character:")
    userIndex = int(input("Enter an index from where to start the search:"))
    index = findChar (userStr, userChar[0], userIndex)
    if index == -1:
        print("This specific character cannot be found in the sentence.")
    else :
        print("This specific character has been found in the sentence, at index: ", index)


if __name__ == "__main__":
    main()
