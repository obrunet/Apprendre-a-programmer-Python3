# A partir de l'exercice prédécent, script qui déremine si une chaine de caractères donnée est un palindrôme.
# i.e la chaine peut se lire indifféremment dans un sens ou dans l'autre

# str =? reverse str

str1 = "kayak"
str1rev = ""                           # assigning a null string needed before using the var.

i , j = 1, len(str1)                    # i increasing index of str1, j decreasing index of str2
while i <= len(str1):
    str1rev = str1rev + str1[j-1]         # j-1 -> offset between index & length
    i, j= i+1, j-1
if str1 == str1rev:
    print(str1, "is a palindrome")
else:
    print(str1, "isn't a palindrome")