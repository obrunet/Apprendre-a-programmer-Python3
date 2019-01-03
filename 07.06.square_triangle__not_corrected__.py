# Complétez le module de fonctions graphiques dessins_tortue.py décrit à la page 72. 
# Commencez par ajouter un paramètre angle à la fonction carre(), 
# de manière à ce que les carrés puissent être tracés dans différentes orientations. 
# Définissez ensuite une fonction triangle(taille, couleur, angle) capable de dessiner un triangle équilatéral d’une taille, 
# d’une couleur et d’une orientation bien déterminées. 
# Testez votre module à l’aide d’un programme qui fera appel à ces fonctions à plusieurs reprises, 
# avec des arguments variés pour dessiner une série de carrés et de triangle


from turtle import *

def carre(taille, couleur, angle):    
    color(couleur)    
    c = 0
    right(angle)
    while c < 4:        
        forward(taille)        
        right(90)        
        c = c + 1 


def triangle(taille, couleur, angle):
    color(couleur)    
    c = 0
    right(angle)
    while c < 3:        
        forward(taille)        
        right(120)        
        c = c + 1 

def main():
    carre(90, 'red', 90)
    forward(100) 
    triangle(20, 'yellow', 120)
    forward(100)
    carre(120, 'blue', 45)
    forward(100)
    triangle(200, 'black', 30)

if __name__ == "__main__":
    main()