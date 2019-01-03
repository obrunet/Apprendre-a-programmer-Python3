# Déterminez vous-même ce qui se passe, dans la technique de slicing, lorsque l’un ou
# l’autre des indices de découpage est erroné, et décrivez cela le mieux possible. (Si le second
# indice est plus petit que le premier, par exemple, ou bien si le second indice est
# plus grand que la taille de la chaîne).

aLongStr = "This is a long sentence used for different tests..."

print(aLongStr)
print("The length of the string is:", len(aLongStr))
 
print(aLongStr[1], aLongStr[3], aLongStr[7], aLongStr[11])      # should display h space g o
print(aLongStr[-1], aLongStr[-3], aLongStr[-5])                 # should display . . t
print(aLongStr[3:9])                                            # should display 6 char form 's'
# problem here print(aLongStr[-1:-5])                                          # should display 4 char reversly from . to s

print(aLongStr + (" zut" *4))                                   # example of multiple concatenation

## answers to the exercice
print(aLongStr[8:6])                                            # doesn't display anything
print(aLongStr[20:65])                                          # display the string form the 20th char to the end

