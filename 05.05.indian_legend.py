# Calcule le nbre de grain de riz sur chacune des 64 cases d'un échéquier sachant que l'on pose
# 1 grain sur la 1ère case
# 2 grains sur la 2ème case
# 4 grains sur la 3ème case
# 8 grains sur la 4ème case etc...
# donner le nbre exact entier et en notation scientifique

nbrGrain = nbCase = 1
for nbCase in range (1, 65):
    print("Case", nbCase, "\tNbr of grain =", nbrGrain, "\tor", float(nbrGrain) )
    nbrGrain , nbCase = nbrGrain*2, nbCase+1