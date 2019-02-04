# Écrivez un script qui crée un mini-système de base de données fonctionnant à l’aide d’un dictionnaire, dans lequel vous mémoriserez les noms 
# d’une série de copains, leur âge et leur taille. Votre script devra comporter deux fonctions : la première pour le remplissage du dictionnaire, 
# et la seconde pour sa consultation. Dans la fonction de remplissage, utilisez une boucle pour accepter les données entrées par l’utilisateur. 
# Dans le dictionnaire, le nom de l’élève servira de clé d’accès, et les valeurs seront constituées de tuples (âge, taille), 
# dans lesquels l’âge sera exprimé en années (donnée de type entier), et la taille en mètres (donnée de type réel). 
# La fonction de consultation comportera elle aussi une boucle, dans laquelle l’utilisateur pourra fournir un nom quelconque 
# pour obtenir en retour le couple « âge, taille » correspondant. Le résultat de la requête devra être une ligne de texte bien formatée, 
# telle par exemple : « Nom : Jean Dhoute - âge : 15 ans - taille : 1.74 m ». 

def consult_db():     
    while 1:         
        name = input("Enter a name (or press <enter> to quit): ")         
        if name == "":             
            break         
        if name in dict:                 
            item = dict[name]             
            age, height = item[0], item[1]             
            print("name: {} - age: {} years old - height: {} m.".format(name, age, height))        
        else:             
            print("unknown name...not in the db...") 

def fill_db():     
    while 1:         
        name = input("Enter the name (or press <enter> to quit=: ")         
        if name == "":             
            break         
        age = int(input("Enter an age (integer): "))         
        height = float(input("Enter a height (float in meters): "))        
        dict[name] = (age, height)     
        
if __name__ == "__main__":      
    dict ={} 
    while 1:     
        user_choice = input("Choose between the folowing actions : (F)ill - (C)onsult - (Q)uit: ")     
        if user_choice.upper() == 'Q':         
            break    
        elif user_choice.upper() == 'F':         
            fill_db()     
        elif user_choice.upper() == 'C':         
            consult_db()