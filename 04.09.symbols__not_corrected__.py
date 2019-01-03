# Programme qui affiche la suite de symboles suivante :
#   *
#   **
#   ***
#   ****
#   *****
#   ******
#   *******

i=1
while i<8:
    j=0
    while j<i:
        print("*", end="")
        j=j+1
    print("\n")
    i=i+1