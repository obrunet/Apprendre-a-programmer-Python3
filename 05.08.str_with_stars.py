# REcopie une chaine (dans une nouvelle variable), en insérant des astérisques entre les caractères
# gaston -> g*a*s*t*o*n

str1 = "efffffffeffffffffffeffffffffffe"
str2 = str1[0]                              # assignement of str2 needed before using it

i = 1 #, j = 0, 0
while i<len(str1):
    str2 = str2 + "*" + str1[i]
    i = i+1
print(str2)


#    str2[j] = str1[i]
#    str2[j+1] = "*"
#    i, j = i+1, j+2