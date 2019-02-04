# Vous disposez d’une liste de nombres entiers quelconques, certains d’entre eux étant présents en plusieurs exemplaires. 
# Écrivez un script qui recopie cette liste dans une autre, en omettant les doublons. La liste finale devra être triée. 

initialList = [1,2,3,4,4,8,4,4,5,6,7,8,9,1,1,8,1,2,3,4,10,15]
print("Initial list:", initialList)

finalList = []

for elt in initialList:
    if elt not in finalList:         # if not (elt in finalList):
        finalList.append(elt)

finalList.sort()
print("Final list:", finalList)