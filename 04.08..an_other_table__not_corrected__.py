# Calcule les 50 premiers temres de la table de multipliation par 13, mais n'affiche que ceux qui sont des multiples de 7

for i in range (1,51):
    nb = i*13
    if nb%7 == 0:
        print (nb)


""" Side note: the following snippets with a while loop also works 
i=1
while i<51:
    nb = i*13
    if nb%7 == 0:
        print (nb)
    i=i+1
"""



""" result
91
182
273
364
455
546
637
"""