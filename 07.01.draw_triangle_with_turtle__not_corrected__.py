# Importez le module turtle pour pouvoir effectuer des dessins simples. 
# Vous allez dessiner une série de triangles équilatéraux de différentes couleurs. 
# Pour ce faire, définissez d’abord une fonction triangle() capable de dessiner un triangle d’une couleur bien déterminée 
# (ce qui signifie donc que la définition de votre fonction doit comporter un paramètre pour recevoir le nom de cette couleur). 
# Utilisez ensuite cette fonction pour reproduire ce même triangle en différents endroits, en changeant de couleur à chaque fois.

# warning : Pylint detect some var undefined, and unused import but the code works fine...

from turtle import *

choosenColor1 = 'red'
choosenColor2 = 'blue'
side1 = 50
side2 = 160

def drawTriangle (userColor, side):
    color(userColor)
    forward(side)
    left(120)
    forward(side)
    left(120)
    forward(side)

def main():
    drawTriangle(choosenColor1, side1)
    forward(-100)
    drawTriangle(choosenColor2, side2)

if __name__ == "__main__":
    main()




""" EXAMPLE SHOWING THAT THE TURTLE MODULE WORKS FINE DESPITE PROBLEMS WITH PYLINT
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

 """





""" EXAMPLE :

import turtle as tu
 
def polygone(long,nbcotes) :
    for i in range(nbcotes) :
        tu.fd(long)
        tu.rt(360/nbcotes)
 
def frise(ang,long,nbcotes) :
    for i in range(720//ang) :
        polygone(long,nbcotes)
        tu.lt(ang)
 
def main() :
    tu.setup(400,400) # Facultatif
    tu.reset()
    tu.speed(0)
    tu.tracer(50,0)
    frise(3,80,5) 
    tu.update()
 
if __name__=='__main__' : main() """