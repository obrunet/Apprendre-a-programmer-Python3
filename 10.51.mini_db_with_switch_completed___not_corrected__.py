# Améliorez encore le script de l’exercice précédent, en utilisant un dictionnaire pour diriger le flux d’exécution du programme 
# au niveau du menu principal. Votre programme affichera par exemple : Choisissez : 
#   (R)écupérer un dictionnaire préexistant sauvegardé dans un fichier 
#   (A)jouter des données au dictionnaire courant 
#   (C)onsulter le dictionnaire courant 
#   (S)auvegarder le dictionnaire courant dans un fichier 
#   (T)erminer :
# Suivant le choix opéré par l’utilisateur, vous effectuerez alors l’appel de la fonction correspondante 
# en la sélectionnant dans un dictionnaire de fonctions.


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
            print("___ unknown name...not in the db ___ ") 


def fill_db():     
    while 1:         
        name = input("Enter the name (or press <enter> to quit=: ")         
        if name == "":             
            break         
        age = int(input("Enter an age (integer): "))         
        height = float(input("Enter a height (float in meters): "))        
        dict[name] = (age, height)     


def save_file():     
    f = input("Enter the file name where the db will be saved: ")     
    ofi = open(f, "w")                                           
    # write a first line as a mark in order to identify the right file     
    ofi.write("Exercice_10.50\n")                                
    # parse the whole dictionnary which is converted in a list first     
    for key, val in list(dict.items()):                         
        # use string format to create the backup         
        ofi.write("{}@{}#{}\n".format(key, val[0], val[1]))     
    ofi.close() 

def read_file():     
    f = input("Enter the name of the backup file: ")     
    try: 
        ofi = open(f, "r")     
    except:         
        print("___  no such file ___ ")         
        return                                                          
    # checks if the file is the right one     
    mark = ofi.readline()     
    if mark != "Exercice_10.50\n":        
        print("___  Incorrect file type ___ ")        
        return                                                      
    # reads lines of the file     
    while 1:         
        line = ofi.readline()         
        if line =='':                                           # detects EOF             
            break         
        record = line.split("@")                                # restitution d'une liste [clé,valeur]         
        key = record[0]         
        val = record[1][:-1]                                    # without the last car (CRLF)        
        data = val.split("#")                                   # converts to a list [age, weight]         
        age, height = int(data[0]), float(data[1])         
        dict[key] = (age, height)                               # converts to a dict     
    ofi.close()


if __name__ == "__main__":      
    dict ={}
    read_file() 
    user_choice_dict = []
    #input_str = "'Choose between the folowing actions :', '\n', '- (F)ill','\n', '- (C)onsult','\n', '- (Q)uit','\n', '-> answer:'" 
#   (R)écupérer un dictionnaire préexistant sauvegardé dans un fichier 
#   (A)jouter des données au dictionnaire courant 
#   (C)onsulter le dictionnaire courant 
#   (S)auvegarder le dictionnaire courant dans un fichier 
#   (T)erminer
    
    while 1:
        print('Choose between the folowing actions :', '\n', '- (F)ill','\n', '- (C)onsult','\n', '- (Q)uit','\n') 
        user_choice = input('-> answer:')      
        if user_choice.upper() == 'Q':         
            break    
        elif user_choice.upper() == 'F':         
            fill_db()     
        elif user_choice.upper() == 'C':         
            consult_db()
    save_file()