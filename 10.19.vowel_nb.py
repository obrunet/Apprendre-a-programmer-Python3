# Écrivez une fonction compteVoyelles(phrase), qui renvoie le nombre de voyelles contenues dans une phrase donnée. 

def vowelNb (s):
    vNb = 0
    for c in s:
        if c in "aeiouyAEIOUY":
            vNb += 1
    return vNb

userSent = str(input("Please enter a sentence with several vowels: "))
print("There are", vowelNb(userSent), "vowels in your sentence!")
