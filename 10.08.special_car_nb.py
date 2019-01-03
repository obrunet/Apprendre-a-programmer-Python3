# Écrivez un script qui recherche le nombre de caractères "e", "é", "è", "ê", "ë"  contenus dans une phrase donnée.

def specialCarNb (carac, sentence):
    nbCar = 0
    for c in sentence:
        if c == carac:
            nbCar += 1
    return (nbCar)

def main():
    specialCars, userSentence = "eéèê", input("Please enter a sentence with several caracters such as eéèê: ")
    for car in specialCars:
        print("The number of caracter:", car, "in your sentence is:", specialCarNb(car, userSentence))

if __name__ == "__main__":
    main()