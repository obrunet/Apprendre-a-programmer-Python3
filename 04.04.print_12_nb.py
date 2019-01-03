# Ecriver un programme qui affiche une suite de 12 nb dont chaque terme soit égal au trimple du terme précédent

nb = 1                                  # initialization for the first value of the loop

for i in range(1,13):                   # until 13 in oder to include i = 12
    print("i = ", i, "terme = ", nb)
    nb = i*3                            # the line is placed after the print so that the previous value of i is multiplied by 3