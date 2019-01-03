# Affiche les 20 premiers termes de la table de multiplication par 7 en signalant au passage (à l'aide d'une astérisque) ceux qui sont des multiples de 3
# exemple : 7 14 21 * 28 35 42 49 ...

for i in range (1,21):      # i is incremented at the end of the loop -> 21
    nb = i*7
    print (nb, end=" ")     # end=" " allow to canceal the CLRF by default
    if i%3 == 0:
        print("*", end=" ") 
      
# Side note : 7 is a prime nb so you can check if i%3 otherwise one need to verify nb%3