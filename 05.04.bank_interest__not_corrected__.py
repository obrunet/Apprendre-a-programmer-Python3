# Calcule les intérêts accumulés chaque année pendant 20 ans, par  capitalisation d'une somme de 100 euros placée en banque au taux fixe de 4.3%

montantInitial = 100
montantFinal = montantInitial
taux = 1.043
nbreAnnees = 20

for i in range(1,(nbreAnnees+1)):
    montantFinal = montantFinal*taux
    print("Fin d'année", i, "\tCapital =", montantFinal, "\tIntérêts accumulés =", (montantFinal-montantInitial))