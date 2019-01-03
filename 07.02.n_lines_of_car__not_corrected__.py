#  Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca

def lineCar(n, ca):
    i , strcar = 0, ""
    while i < n:
        strcar = strcar + ca
        i = i+1
    return (strcar)

def main ():
    print("Enter a caracter:", end=" ")
    carac = str(input())
    print("Enter a number", end=" ")
    nb = int(input())
    print(lineCar(nb, carac))

if __name__ == "__main__":
    main()

