# Écrivez une fonction voyelle(car), qui renvoie « vrai » si le caractère fourni en argument est une voyelle.

def isVowel (c):
    if c in "aeiouyAEIOUY":
        return True
    else:
        return False

userCar = str(input("Please enter a single caracter: "))
if isVowel(userCar):
    print("You've entered a vowel.")
else:
    print("You've entered a consonnant")
