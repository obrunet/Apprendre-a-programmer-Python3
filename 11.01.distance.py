# Écrivez une fonction distance() qui permette de calculer la distance entre deux points. 
# (Il faudra vous rappeler le théorème de Pythagore !) Cette fonction attendra évidemment deux objets Point() comme arguments.

import math

class Point(object):
    "Class definition of a geometrical point with x, y"

def print_coord(p):
    "Print the coordinates of a point"
    print("x = {} & y = {}".format(p.x, p.y))

def distance(p1, p2):
    "Calculate the distance between 2 points"
    d = math.sqrt( math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
    return d

if __name__ == "__main__":
    p1, p2 = Point(), Point()
    p1.x, p2.x = 3.0, 9.0
    p1.y, p2.y = 4.0, 5.0

    #print(p1.__doc__)
    #print(Point.__doc__)
    #print(distance.__doc__)
    print(p1.x + p1.y)
    print_coord(p1)
    print("The distance between p1 a p2 is equal to: ", distance(p1, p2)) 
