# Définissez une classe Cercle(). Les objets construits à partir de cette classe seront des cercles de tailles variées. 
# En plus de la méthode constructeur (qui utilisera donc un paramètre rayon), vous définirez une méthode surface(), qui devra renvoyer la surface du cercle. 
# Définissez ensuite une classe Cylindre() dérivée de la précédente. 
# Le constructeur de cette nouvelle classe comportera les deux paramètres rayon et hauteur. 
# Vous y ajouterez une méthode volume() qui devra renvoyer le volume du cylindre (rappel : volume d’un cylindre = surface de section × hauteur). 
# Exemple d’utilisation de cette classe : 
# >>> cyl = Cylindre(5, 7) 
# >>> print(cyl.surface()) 78.54 
# >>> print(cyl.volume()) 549.78 


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

    def __init__(self, name, base_radius, height):
        "Initializes a Cylinder object"
        Circle.__init__(self, name, base_radius)
        self.height = height

    def volume(self):
        "Retunrs the cylinder volume"
        return(self.height * self.area())


if __name__ == "__main__":
    cyl = Cylinder('cyl_dude', 5, 7)
    print("The area of the cylinder named '{}' is equal to: {:.1f}".format(cyl.name, cyl.area()))
    print("The volume of the cylinder named '{}' is equal to: {:.1f}".format(cyl.name, cyl.volume()))