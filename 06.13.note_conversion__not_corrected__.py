# Convertir une note scolaire N quelconque, entrée par l’utilisateur sous forme de points (par exemple 27 sur 85), 
# en une note standardisée suivant le code ci-dessous :          
# Note                Appréciation          
# N >= 80 %                 A          
# 80 % > N >= 60 %          B          
# 60 % > N >= 50 %          C          
# 50 % > N >= 40 %          D          
# N < 40 %                  E 

print("Enter a note:", end=" ")
note = int(input())
print("On how many:", end=" ")
base = int(input())

fNote = note / base

if fNote < 0.4:
    print("Appreciation E")
else:
    if fNote < 0.5:
        print("Appreciation D")
    else:
        if fNote < 0.6:
            print("Appreciation C")
        else:
            if fNote < 0.8:
                print("Appreciation B")
            else:                               # in this cas fNote >= 0.8
                print("Appreciation A")

print("--------------------- Other solution ---------------------")         # an other solution

# N >= 80 %                 A          
# 80 % > N >= 60 %          B          
# 60 % > N >= 50 %          C          
# 50 % > N >= 40 %          D          
# N < 40 %                  E 

if fNote >= 0.8:
    print("Appreciation A")
if 0.6 <= fNote and fNote < 0.8 :
    print("Appreciation B")
if 0.5 <= fNote and fNote < 0.6 :
    print("Appreciation C")
if 0.4 <= fNote and fNote < 0.5 :
    print("Appreciation D")
if fNote < 0.4 :
    print("Appreciation E")