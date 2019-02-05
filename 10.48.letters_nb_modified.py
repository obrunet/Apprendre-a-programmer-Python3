# Modifiez le script précédent afin qu’il établisse une table des occurrences de chaque mot dans le texte. 
# Conseil : dans un texte quelconque, les mots ne sont pas seulement séparés par des espaces, mais également par divers signes de ponctuation. 
# Pour simplifier le problème, vous pouvez commencer par remplacer tous les caractères non-alphabétiques par des espaces, 
# et convertir la chaîne résultante en une liste de mots à l’aide de la méthode split().


text = "sfqgkplvemlk tgposj^^f gz*m!ektpskA fpzkBrlpz^ fsfCnblmq:fpoir.Dzertyuiops dfFghjklm xcvbnoiuytr elkjhgfdnbvcfghjvb"
alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü" 
car_list = ""   
dict ={} 

# converts all non-alpha car to spaces                     
for c in text:     
    c = c.lower()   
    if c in alpha:         
        car_list = car_list + c     
    else:         
        car_list = car_list + ' ' 

word = car_list.split()             # converts the resulting string in a word list 

for w in word:                      # fil the dictionnary
    dict[w] = dict.get(w, 0) +1 
car_list = list(dict.items()) 
car_list.sort()

for item in car_list:     
    print("{} : {}".format(item[0], item[1])) 
