# Définissez une classe Satellite() qui permette d’instancier des objets simulant des satellites artificiels lancés dans l’espace, autour de la terre. 
# Le constructeur de cette classe initialisera les attributs d’instance suivants, avec les valeurs par défaut indiquées : masse = 100,  vitesse = 0. 
# Lorsque l’on instanciera un nouvel objet Satellite(), on pourra choisir son nom, sa masse et sa vitesse. 
# Les méthodes suivantes seront définies : 
# • impulsion(force, duree) permettra de faire varier la vitesse du satellite. Pour savoir comment, rappelez-vous votre cours de physique : 
#   la variation de vitesse Δv subie par un objet de masse m soumis à l’action d’une force F pendant un temps t vaut Δv= F×t / m . 
#   Par exemple : un satellite de 300 kg qui subit une force de 600 Newtons pendant 10 secondes voit sa vitesse augmenter (ou diminuer) de 20 m/s. 
# • affiche_vitesse() affichera le nom du satellite et sa vitesse courante.
# • energie() renverra au programme appelant la valeur de l’énergie cinétique du satellite. 
#   Rappel : l’énergie cinétique se calcule à l’aide de la formule Ec=m×v2 / 2 
# 
# Exemples d’utilisation de cette classe : 
# >>> s1 = Satellite('Zoé', masse =250, vitesse =10) 
# >>> s1.impulsion(500, 15) >>> s1.affiche_vitesse() vitesse du satellite Zoé = 40 m/s. 
# >>> print(s1.energie()) 200000 
# >>> s1.impulsion(500, 15) 
# >>> s1.affiche_vitesse() vitesse du satellite Zoé = 70 m/s. 
# >>> print(s1.energie()) 612500

class Satellite(object):
    "Class that simulates an artificial satellite in space around the earth"

    def __init__(self, name, mass = 100, velocity = 0):
        "Initializes a Satelitte object"
        self.name = name
        self.mass = mass
        self.velocity = velocity

    def impulsion(self, strength, duration):
        "Satellite method that changes the velocity according to strength and duration"
        self.velocity += strength * duration / self.mass

    def display_velocity(self):
        "Satellite method that displays its name velocity"
        print("The satellite named {} has a velocity of {} m/s".format(self.name, self.velocity))
    
    def energy(self):
        "Satellite method that returns its cinetic energy"
        energy = self.mass * self.velocity**2 / 2
        return energy


if __name__ == "__main__":
    s1 = Satellite('Zoé', mass = 250, velocity = 10)
    s1.impulsion(500, 15)
    s1.display_velocity()
    print(s1.energy())
    s1.impulsion(500, 15)
    s1.display_velocity()
    print(s1.energy())