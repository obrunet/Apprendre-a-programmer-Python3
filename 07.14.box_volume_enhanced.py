# Modifiez la fonction volBoite(x1,x2,x3) que vous avez définie dans un exercice précédent, 
# de manière à ce qu’elle puisse être appelée avec trois, deux, un seul, ou même aucun argument. 
# Utilisez pour ceux ci des valeurs par défaut égales à 10. 
# Par exemple : 
# print(volBoite()) doit donner le résultat : 1000 
# print(volBoite(5.2)) doit donner le résultat : 520.0 
# print(volBoite(5.2, 3)) doit donner le résultat : 156.0 


def boxVolume (a=10, b=10, c=10):
    return (a*b*c)

def main():
    print ("The volum of the box is equal to:", boxVolume())
    print ("The volum of the box is equal to:", boxVolume(5.2))
    print ("The volum of the box is equal to:", boxVolume(5.2, 3))
    print ("The volum of the box is equal to:", boxVolume(5.2, 3, 12.3))

if __name__ == "__main__":
    main()