import math

class Point(object):
    "Class definition of a geometrical point with x, y"
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def print_coord(self):
        "Print the coordinates of a point"
        print("x = {0} & y = {1}".format(self.x, self.y))

def distance(p1, p2):
    "Calculate the distance between 2 points"
    d = math.sqrt( math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
    return d

if __name__ == "__main__":
    p1, p2 = Point(3.0, 4.0), Point(4.0, 5.0)
    # print(p1.__doc__)   or     print(Point.__doc__)
    # print(distance.__doc__) and   print(Point.print_coord.__doc__)
    print(p1.x + p1.y)
    Point.print_coord(p1)
    print("The distance between p1 and p2 is equal to: {:.2f}".format(distance(p1, p2)))