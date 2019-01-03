# Dans un script, écrivez une fonction qui recherche le nombre de mots contenus dans une phrase donnée.

userSentence = input("Enter a sentence with different words separeted by spaces:")
wordNb = 1

for car in userSentence:
    if car == ' ':
        wordNb += 1
print("The number of words in your sentence is equal to ", wordNb) 