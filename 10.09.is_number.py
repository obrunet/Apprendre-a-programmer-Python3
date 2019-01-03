# Écrivez une fonction estUnChiffre() qui renvoie « vrai », si l’argument transmis est un chiffre, et « faux » sinon. 
# Tester ainsi tous les caractères d’une chaîne en parcourant celle-ci à l’aide d’une boucle for. 


def isNumber(car):
    if car in "0123456789":
        return True
    else:
        return False


userSentence, noNb = input("Please enter a sentence with different types of caracters: "), 1
for car in userSentence:
    if isNumber(car):
        print("In your sentence there is a number")
        noNb = 0
        break
if noNb == 1:
        print("In your sentence there isn't any number")