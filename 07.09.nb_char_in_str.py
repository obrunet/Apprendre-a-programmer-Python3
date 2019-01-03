# Définissez une fonction compteCar(ca,ch) qui renvoie le nombre de fois que l’on rencontre le caractère ca dans la chaîne de caractères ch. 
# Par exemple, l’exécution de l’instruction : print(compteCar(’e’, ’Cette phrase est un exemple’)) doit donner le résultat : 7

def nbOfChar (char, st):
    i, nb = 0, 0
    while i<len (st):
        if st[i] == char:
            nb = nb+1
        i = i+1
    return (nb)

def main():
    print("Please enter a sentence:", end=" ")
    sent = input()
    print(nbOfChar('e', sent))

if __name__ == "__main__":
    main()