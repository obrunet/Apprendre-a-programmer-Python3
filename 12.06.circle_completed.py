# Complétez l’exercice précédent en lui ajoutant encore une classe Cone(), qui devra dériver cette fois de la classe Cylindre(), 
# et dont le constructeur comportera lui aussi les deux paramètres rayon et hauteur. 
# Cette nouvelle classe possédera sa propre méthode volume(), laquelle devra renvoyer le volume du cône 
# (rappel : volume d’un cône = volume du cylindre correspondant divisé par 3). 
# Exemple d’utilisation de cette classe : 
# >>> co = Cone(5,7) 
# >>> print(co.volume()) 183.26 


class Circle(object):
    "Circle class definition"

    def __init__(self, name, radius):
        "Initializes a Circle object"
        self.name = name
        self.radius = radius

    def area(self):
        "Returns the circle area"
        return(3.14 * self.radius **2)


class Cylinder(Circle):
    "Cylinder class definition"

    def __init__(self, name, radius, height):
        "Initializes a Cylinder object"
        Circle.__init__(self, name, radius)
        self.height = height

    def volume(self):
        "Retunrs the cylinder volume"
        return(self.height * self.area())


class Cone(Cylinder):
    "Cone class definition"

    def __init__(self, name, base, height):
        "Initializes a Cone object"
        Cylinder.__init__(self, name, base, height)

    def volume(self):
        "Retunrs the cone volume"
        return(self.height * self.area() / 3)


if __name__ == "__main__":
    co = Cone('cone_dude', 5, 7) 
    print("The volume of the cone named '{}' is equal to: {:.1f}".format(co.name, co.volume()))