# recopie une chaine (dans une nouvelle variable) en l'inversant.

str1 = "abcdefg"
str2 = ""                           # assigning a null string needed before using the var.

i , j = 1, len(str1)                # i increasing index of str1, j decreasing index of str2
while i <= len(str1):
    str2 = str2 + str1[j-1]         # j-1 -> offset between index & length
    i, j= i+1, j-1
print(str2)

# a more elegant solution consist in using only one decreasing index...