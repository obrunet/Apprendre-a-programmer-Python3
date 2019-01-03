# Écrivez une fonction estUneMaj() qui renvoie « vrai » si l’argument transmis est une majuscule. 
# Tâchez de tenir compte des majuscules accentuées !


def isUppercase(car):
    if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False


userSentence, noUpperCase = input("Please enter a sentence with different types of caracters: "), 1
for car in userSentence:
    if isUppercase(car):
        print("In your sentence there is a caracter in uppercase")
        noUpperCase = 0
        break
if noUpperCase == 1:
        print("In your sentence there isn't any caracter in uppercase")