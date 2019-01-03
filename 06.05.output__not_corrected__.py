# Que fait le programme ci-dessous, 
# dans les quatre cas où l’on aurait défini au préalable que la variable a vaut 1, 2, 3 ou 15 ? 
# if a !=2:    
#   print('perdu') 
# elif a ==3:    
#   print('un instant, s.v.p.') 
# else :    
#   print('gagné')

a = 3
if a != 2:    
    print('perdu') 
elif a == 3:    
    print('un instant, s.v.p.') 
else:    
    print('gagné')

# solution:
# a = 1 -> perdu
# a = 2 -> gagné
# a = 3 -> perdu (et non "un instant svp")
# a = 15 -> perdu