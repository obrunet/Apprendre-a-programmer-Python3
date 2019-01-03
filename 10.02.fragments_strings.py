# Découpez une grande chaîne en fragments de 5 caractères chacun. Rassemblez ces
# morceaux dans l’ordre inverse. La chaîne doit pouvoir contenir des caractères accentués.


aLongStr = "This is a long sentence used for different tésts!!"    # 50 char
print("The original string is:\n", aLongStr)
 
revStr = ""
w = 5                           # width of the string fragment (for instance 5 in our case)

i = len(aLongStr)               # index of the last char
while i > 0:
    tempStr = aLongStr[(i-w):i]
    revStr = revStr + tempStr
    i = i - w

print("The string with fragments in the reverse order is:\n", str(revStr))







"""     if i%5 == 0:                 # last char to put in the fragment
        tempStr.append(aLongStr[i])
        revStr.append(tempStr)
        tempStr = ""
    else:
        tempStr.append(aLongStr[i]) """

""" 
    for j in range (1,6):
        
        j += 1
    
    print(aLongStr[20:65]) """
       