# Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres multiples de 3 et de 5 compris entre ces bornes.
# Prendre par exemple a = 0, b = 32 ; le résultat devrait être alors 0 + 15 + 30 = 45. 
# Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5 compris entre les bornes a et b. 
# Avec les bornes 0 et 32, le résultat devrait donc être : 
# 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.

l = [1,0]

while l[0]>l[1]:                        # l[0] != "" & l[1] != "" & 
    print("Entrez les valeurs des 2 bornes (séparées par des virgules):")
    l = list(eval(input()))

i, sum = 0, 0
while i < l[1]:
    if (i%3 == 0) & (i%5 == 0):                 # and don't need brackets
        sum = sum + i
    i = i+1
print ("La somme est:", sum)


#-------------------------------------------------------- variante

i, sum = 0, 0
while i < l[1]:
    if i%3 == 0 or i%5 == 0:                # & remplacé par or
        sum = sum + i
    i = i+1
print ("La somme est:", sum)