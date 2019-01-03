# Ajoutez au module de l’exercice précédent une fonction etoile5() spécialisée dans le dessin d’étoiles à 5 branches. 
# Dans votre programme principal, insérez une boucle qui dessine une rangée horizontale de de 9 petites étoiles de tailles variées 

from turtle import *

def stars5(side, col, angle):    
    color(col)    
    c = 0
    right(angle)
    while c < 5:        
        forward(side)        
        right (180 - (180-2*(360/5)))           # angle of the star = (180-2*(360/5))      
        c = c + 1                               # if you want the turtle to turn ang° you need to provide an angle of (180-ang)

def main():
    beginSide = 20
    i = 0
    while i<9:
        stars5(beginSide, 'red', 0)
        beginSide = beginSide + 5
        i = i+1
        color('white')
        forward(50) 


if __name__ == "__main__":
    main()