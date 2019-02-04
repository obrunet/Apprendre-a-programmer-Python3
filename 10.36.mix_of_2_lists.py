# Soient les listes suivantes : t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
# t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
# Écrivez un petit programme qui insère dans la seconde liste tous les éléments de la
# première, de telle sorte que chaque nom de mois soit suivi du nombre de jours correspondant
# : ['Janvier',31,'Février',28,'Mars',31, etc.].

t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
print("Initial lists t1 & t2:", "\n", t1, "\n", t2, "\n")

i, j = 1, 0

while j < len(t1):
    t2[i:i] = [t1[j]] # et pourquoi ici t2[i:i+1] recopie toute la liste ? cf ex suivant !
    i, j = i+2, j+1

print("Final list:", t2)