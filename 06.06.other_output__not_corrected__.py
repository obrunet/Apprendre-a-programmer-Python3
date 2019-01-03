# Que font ces programmes ? 

"""--------------------------------------------------------------
a = 5     
b = 2     
if (a==5) & (b<2):         
    print('"&" signifie "et"; on peut aussi utiliser\                
                    le mot "and"')
--------------------------------------------------------------
a, b = 2, 4     
if (a==4) or (b!=4):         
    print('gagné')     
elif (a==4) or (b==4):         
    print('presque gagné')
--------------------------------------------------------------
a = 1     
if not a:         
    print('gagné')     
elif a:         
    print('perdu')
-------------------------------------------------------------- """

# pour le 1er : rien ne s'affiche à cause du b<2 car b==2
# pour le 2eme : a==4 faux et b!=4 faux -> pas le 1er if // a==4 faux et b==4 vrai donc vrai avec le ou -> elif et print "presque gagné" 
# pour le 3ème : a=1 -> not a = 0 ou faux -> a différent de 0 -> 'perdu'

