"""
QUESTION (2 solutions possibles)

Vous achetez un couple de souris. Une souris produit une moyenne de 8 souriceaux par portée. 
La gestation dure 3 semaines. Elle est capable de se reproduire à l’âge de 6 semaines. 
Vous voulez maintenir votre population à 550 individus. 

a) Au bout de combien de temps, vous alarmez-vous ? 
b) Vous ne pouvez pas tuer les souris, quel processus mettez-vous en place ?

________________ 1 sur 2 SOLUTION MATHEMATIQUE ________________  

En supposant :
- qu’il y ait autant de mâles que de femelles par portée 
- que celles/ceux s’étant déjà reproduits continuent à faire des petits 
- que le 1er couple vient tout juste de naitre :

Pour une trame de temps t de 3 semaines :
- soit A(t) le nombre de souris ayant 0 à 3 mois -> A(t) = 4C(t-1)
- soit B(t) le nombre de souris ayant 3 à 6 mois -> B(t) = A(t-1)
- soit C(t) le nombre de souris ayant plus de 6 mois donc faisant des petits -> C(t) = C(t-1) + B(t-1)

A(t) + B(t) +C(t)   = 4C(t-1) + A(t-1) + C(t-1) + B(t-1) = T(t) (total au temps t)
                    = 4C(t-1) + T(t-1)
C(t-1)  = C(t-2) + B(t-2)
        = C(t-3) + B(t-3) + B(t-2) or B(t-2) = C(t-3)
        = T(t-3)            Nota: il s'agit d'une "variante" de la suite de Fibonnaci.

donc T(t) = T(t-1) + 4T(t-3) = ceux présents 3 sem. avant + 4 fois ceux en âge de procréer
Conditions initiales T(0) = T(1) = T(2) = 1 

Pour obtenir l'expression fonctionnelle T(t) en fonction de t, 
il s'agit d'une suite linéairement récurrente d’ordre 3 d'équation caractéristique:
T(t+3) - T(t+2) - 4T(t) = 0 donne  x3 - x2 - 4 = 0 = x(x2 - x - 4) = (x-v)(x-y)(x-z)
où v = 0 ; y = (1+ racine (17))/2 et z = (1- racine (17))/2

Les suites phi^n engendrent alors l'espace vectoriel des suites vérifiant T(t) = T(t-1) + 4T(t-3):
T(t) = A x phi^t + B x phi'^t + C x phi''^t
où  phi^t = y
    phi'^t = z avec phi' = - 1 / phi
    phi''^t = v = 0
T(t) = Ay^t + Bz^t avec les conditions initiales T(0) = 0 et T(1) = T(2) = 1
A = 1 / racine (17) et B = -1 / racine (17)

Au final T(t) = (phi^t - phi'^t)/racine (17) avec phi = (1+racine(17))/2 et phi' = - 1 / phi


________________ 2 sur 2 SOLUTION  ALGORITHMIQUE ________________ 

"""

# initialisation pour t>3
T_3 = 1 # T total pour t-3
T_2 = 1 # T total pour t-2
T_1 = 1

for i in range (3, 15):
    T = T_1 + 4*T_3                     # T(t) = T(t-1) + 4T(t-3)
    resultat = "Au temps t = {} - {} semaines, il y a {} couples soit {} souris"
    print(resultat.format(i, i*3, T, T*2))
    # permutation, 3 semaines plus tard
    T_3 = T_2       # ce qui était T-2 devient T-3
    T_2 = T_1       # ce qui était T-1 devient T-2
    T_1 = T         # ce qui était T devient T-1

"""
Au temps t = 3 - 9 semaines, il y a 5 couples soit 10 souris
Au temps t = 4 - 12 semaines, il y a 9 couples soit 18 souris
Au temps t = 5 - 15 semaines, il y a 13 couples soit 26 souris
Au temps t = 6 - 18 semaines, il y a 33 couples soit 66 souris
Au temps t = 7 - 21 semaines, il y a 69 couples soit 138 souris
Au temps t = 8 - 24 semaines, il y a 121 couples soit 242 souris
Au temps t = 9 - 27 semaines, il y a 253 couples soit 506 souris
Au temps t = 10 - 30 semaines, il y a 529 couples soit 1058 souris
Au temps t = 11 - 33 semaines, il y a 1013 couples soit 2026 souris
Au temps t = 12 - 36 semaines, il y a 2025 couples soit 4050 souris
Au temps t = 13 - 39 semaines, il y a 4141 couples soit 8282 souris
Au temps t = 14 - 42 semaines, il y a 8193 couples soit 16386 souris
"""



       
