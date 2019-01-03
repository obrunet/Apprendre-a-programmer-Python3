# Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres n1, n2, n3 fournis en arguments. 
# Par exemple, l’exécution de l’instruction : print(maximum(2,5,4))  doit donner le résultat : 5

def maximum (a, b, c):
    max = a
    if a < b:
        max = b
    if b < c:
        max = c
    return (max)

def main():
    print("Enter a first nb:", end=" ")
    a = float (input())
    print("Enter a second nb:", end=" ")
    b = float (input())
    print("Enter a third nb:", end=" ")
    c = float (input())
    print("The maximum is equal to:", maximum(a, b, c))

if __name__ == "__main__":
    main()