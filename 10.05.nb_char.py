# Écrivez une fonction compteCar() qui compte le nombre d’occurrences d’un caractère
# donné dans une chaîne. Ainsi :
# print(compteCar("ananas au jus","a"))
# devra afficher : 4
# print(compteCar("Gédéon est déjà là","é"))
# devra afficher : 3.


def findNbChar (sentence, speChar):
    i, j = 0, 0
    while i < len(sentence):
        if sentence[i] == speChar:
            j += 1
        i += 1
    return(j)


def main():
    userStr, userChar = input ("Please enter a sentence:"), input ("Then enter a char:")
    print("The number of this specific character found in the sentence is:", findNbChar (userStr, userChar[0]))

main()

