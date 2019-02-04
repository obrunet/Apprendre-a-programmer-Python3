# Écrivez un script qui permette d’obtenir à l’écran les 15 premiers termes des tables de multiplication 
# par 2, 3, 5, 7, 11, 13, 17, 19 (ces nombres seront placés au départ dans 
# une liste) sous la forme d’une table similaire à la suivante :  
# 2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  
# 3   6   9  12  15  18  21  24  27  30  33  36  39  42  45  
# 5  10  15  20  25  30  35  40  45  50  55  60  65  70  75    
# etc. 


tableList = [2, 3, 5, 7, 11, 13, 17, 19]

def printMulTable(nb):
    i, mTable = 1, []
    while i <= 15:
        mTable.append(nb*i)
        i += 1
    print(mTable)

def parseTable(tList):
    for i in tList:
        printMulTable(i)

if __name__ == "__main__":
    parseTable(tableList)