# Définissez une fonction surfCercle(R). 
# Cette fonction doit renvoyer la surface (l’aire) d’un cercle dont on lui a fourni le rayon R en argument. 
# Par exemple, l’exécution de l’instruction : print(surfCercle(2.5))  doit donner le résultat : 19.63495..


def circleArea(r):
    return (r*r*3.14159)

def main():
    print("Enter a circle's radius:", end=" ")
    print("The circle's area is equal to:", circleArea (float(input())) )

if __name__ == "__main__":
    main()
