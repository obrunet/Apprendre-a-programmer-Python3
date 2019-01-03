# Ecrivez un programme qui affiche les 20 premiers termes de la table de multipiation par 7

for i in range(1,21):                       # i should go to 21 because the print function is placed before inc of i (in order to print the first value) 
    print ("line #", i, "   ", i*7)
    i = i+1