# Définissez une classe Domino() qui permette d’instancier des objets simulant les pièces d’un jeu de dominos. 
# Le constructeur de cette classe initialisera les valeurs des points présents sur les deux faces A et B du domino 
# (valeurs par défaut = 0). Deux autres méthodes seront définies : 
# • une méthode affiche_points() qui affiche les points présents sur les deux faces ; 
# • une méthode valeur() qui renvoie la somme des points présents sur les 2 faces. 
# Exemples d’utilisation de cette classe : 
# >>> d1 = Domino(2,6) 
# >>> d2 = Domino(4,3) 
# >>> d1.affiche_points() face A : 2  face B : 6 
# >>> d2.affiche_points() face A : 4  face B : 3 
# >>> print("total des points :", d1.valeur() + d2.valeur()) 15 
# >>> liste_dominos = [] 
# >>> for i in range(7): ...    liste_dominos.append(Domino(6, i)) 
# >>> print(liste_dominos[3]) <__main__.Domino object at 0xb758b92c> etc. 

class Domino(object):
    "Class to create pièces of the domino game, with 2 faces"
    def __init__(self, face_a = 0, face_b = 0): 
        self.face_a = face_a
        self.face_b = face_b
    
    def display_points(self):
        "Displays the points of each face of the domino"
        print("Points nb on face A = {}, and on face B = {}".format(self.face_a, self.face_b))
    
    def sum_values(self):
        "Retunrs the sums of the values on each face"
        return(self.face_a + self.face_b)


if __name__ == "__main__":
    d1 = Domino(2, 6)
    d2 = Domino(4, 3)
    d1.display_points()
    d2.display_points()
    print("Sum of points: ", d1.sum_values() + d2.sum_values())
    domino_list = [Domino(6,i) for i in range(7)]
    print(domino_list[3])
    domino_list[3].display_points()

