# Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d’une boîte parallélépipédique 
# dont on fournit les trois dimensions x1, x2, x3 en arguments. 
# Par exemple, l’exécution de l’instruction : print(volBoite(5.2, 7.7, 3.3))  doit donner le résultat : 132.132. 

def boxVolume (a, b, c):
    return (a*b*c)

def main():
    print("Please enter the width of a box :", end=" ")
    a = float(input())
    print("Please enter the height of the box :", end=" ")
    b = float(input())
    print("Please enter the depth of the box :", end=" ")
    c = float(input())
    print ("The volum of the box is equal to:", boxVolume(a, b, c))

if __name__ == "__main__":
    main()
