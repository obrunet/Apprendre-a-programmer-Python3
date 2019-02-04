# Écrivez un script qui recherche le mot le plus long dans une phrase donnée 
# (l’utilisateur du programme doit pouvoir entrer une phrase de son choix). 

inputStr = input("Enter a long sentence with serveral words: ")
inputList = inputStr.split(" ")
# print(inputList)

longest_word, length = "", 0
for word in inputList:
    if len(word) > length:
        length = len(word)
        longest_word = word

result = "The longest word is {} with {} char"
print(result.format(longest_word, len(longest_word)))