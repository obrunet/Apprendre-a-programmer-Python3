# Définissez une fonction nomMois(n) qui renvoie le nom du n-ième mois de l’année. 
# Par exemple, l’exécution de l’instruction : 
# print(nomMois(4)) doit donner le résultat :  Avril. 

monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def nameMonth (index):
    return (monthList[index-1])

def main():
    print("Choose the number of a month in year:", end=" ")
    print("The corresponding month is", nameMonth(int(input())))

if __name__ == "__main__":
    main()