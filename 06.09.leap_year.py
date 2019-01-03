# Déterminer si une année (dont le millésime est introduit par l’utilisateur) est bissextile ou non. 
# Une année A est bissextile si A est divisible par 4. 
# Elle ne l’est cependant pas si A est un multiple de 100, à moins que A ne soit multiple de 400.

print("Enter a year:")
enteredYear = int(input())

if enteredYear%400 == 0:
    print("This is a leap year")
elif enteredYear%100 ==0:
    print("This is NOT a leap year")
elif enteredYear%4 == 0:
    print("This is a leap year")
else:
    print("This is NOT a leap year")