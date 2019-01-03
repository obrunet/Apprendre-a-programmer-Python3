# Définissez une fonction inverse(ch) qui permette d’inverser les l’ordre des caractères d’une chaîne quelconque. 
# La chaîne inversée sera renvoyée au programme appelant.


def reverseString (string):
    i , revStr = len(string), ""
    while i > 0:
        revStr, i = revStr + string[i-1], i-1
    return(revStr) 

def main():
    print("Please enter a sentence:", end=" ")
    print("The reversed string is :", reverseString(str(input())))

if __name__ == "__main__":
    main()