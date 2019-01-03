# Définissez une fonction compteMots(ph) qui renvoie le nombre de mots contenus dans la phrase ph. 
# On considère comme mots les ensembles de caractères inclus entre des espaces.

def nbWordsSentence (string):
    i , nbWord = 0, 0
    while i < len(string):
        if string[i] == " ":
            nbWord = nbWord+1
        i = i+1
    return(nbWord+1)                # Sentences are usually terminated by punctuation, so nbrWords = nbSpaces +1  

def main():
    print("Please enter a sentence:", end=" ")                              # This is a long sentence with many words!
    print("There are", nbWordsSentence(str(input())), "word(s) in this sentence")

if __name__ == "__main__":
    main()