# Définissez une classe Voiture() qui permette d’instancier des objets reproduisant le comportement de voitures automobiles. 
# Le constructeur de cette classe initialisera les attributs d’instance suivants, avec les valeurs par défaut indiquées : 
# marque = 'Ford',  couleur = 'rouge',  pilote = 'personne',  vitesse = 0. 
# Lorsque l’on instanciera un nouvel objet Voiture(), on pourra choisir sa marque et sa couleur, mais pas sa vitesse, ni le nom de son conducteur. 
# Les méthodes suivantes seront définies : 
# • choix_conducteur(nom) permettra de désigner (ou changer) le nom du conducteur. 
# • accelerer(taux, duree) permettra de faire varier la vitesse de la voiture. La variation de vitesse obtenue sera égale au produit : taux × duree. 
#   Par exemple, si la voiture accélère au taux de 1,3 m/s pendant 20 secondes, son gain de vitesse doit être égal à 26 m/s. 
#   Des taux négatifs seront acceptés (ce qui permettra de décélérer). 
#   La variation de vitesse ne sera pas autorisée si le conducteur est ’personne’. 
# • affiche_tout() permettra de faire apparaître les propriétés présentes de la voiture, 
#   c’est-à-dire sa marque, sa couleur, le nom de son conducteur, sa vitesse. 
# 
# Exemples d’utilisation de cette classe : 
# >>> a1 = Voiture('Peugeot', 'bleue') 
# >>> a2 = Voiture(couleur = 'verte') 
# >>> a3 = Voiture('Mercedes') >>> a1.choix_conducteur('Roméo') 
# >>> a2.choix_conducteur('Juliette') >>> a2.accelerer(1.8, 12) 
# >>> a3.accelerer(1.9, 11) Cette voiture n'a pas de conducteur ! 
# >>> a2.affiche_tout() Ford verte pilotée par Juliette, vitesse = 21.6 m/s. 
# >>> a3.affiche_tout() Mercedes rouge pilotée par personne, vitesse = 0 m/s. 

class Car(object):
    "Defines the car class - attributes: brand, color, driver, speed - methods: driver_choice, accelerate, displays infos"
    def __init__(self, brand = 'Ford', color = 'red'):
        "Initializes a car object"
        self.brand = brand
        self.color = color
        self.driver = 'nobody'
        self.speed = 0.0

    def driver_choice(self, name):
        "Choose the driver's name"
        self.driver = name

    def accelerate(self, rate, duration):
        "Accelerate or decelerate"
        if self.driver != 'nobody':
            self.speed += rate/duration
        else:
            print("This car doesn't have any driver !")

    def displays_infos(self):
        "Displays all infos about the car"
        print("Car infos - brand's name: {}, color: {}, driver's name: {}, speed: {:.2f} m/s".format(self.brand, self.color, self.driver, self.speed))


if __name__ == "__main__":
    c1 = Car('Peugeot', 'blue')
    c1.driver_choice('Roméo')
    c1.displays_infos()

    c2 = Car(color = 'green')
    c2.driver_choice('Juliette')
    c2.accelerate(-1.8, 12)
    c2.displays_infos()

    c3 = Car('Mercedes')
    c3.accelerate(1.9, 11)
    c3.displays_infos()