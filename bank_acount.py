# Définissez une classe Compte_bancaire(), qui permette d’instancier des objets tels que
# compte1, compte2, etc. Le constructeur de cette classe initialisera deux attributs
# d’instance nom et solde, avec les valeurs par défaut ’Dupont’ et 1000.
# Trois autres méthodes seront définies :
# • depot(somme) permettra d’ajouter une certaine somme au solde ;
# • retrait(somme) permettra de retirer une certaine somme du solde ;
# • affiche() permettra d’afficher le nom du titulaire et le solde de son compte.
# Exemples d’utilisation de cette classe :
#     compte1 = Compte_bancaire('Duchmol', 800)
#     compte1.depot(350)
#     compte1.retrait(200)
#     compte1.affiche()
# Le solde du compte bancaire de Duchmol est de 950 euros.
#     compte2 = Compte_bancaire()
#     compte2.depot(25)
#     compte2.affiche()
# Le solde du compte bancaire de Dupont est de 1025 euros.

class Compte_bancaire(object):
    "Définition de la classe 'compte bancaire'"

    def __init__(self, nom = 'Dupont', solde = 1000):
        "Méthode d'initialisation: défini les attributes nom & solde"
        self.nom = nom
        self.solde = solde

    def depot(self, credit):
        "Ajout le montant du dépot au solde du compte"
        self.solde += credit

    def retrait(self, debit):
        "Retire le montant du retrait au solde du compte"
        self.solde -= debit

    def affiche(self):
        "Affiche le montant du solde du compte"
        print("Le solde du compte de M. {} est de {} euros".format(self.nom, self.solde))


if __name__ == "__main__":

    #print(Compte_bancaire.__doc__)
    c1 = Compte_bancaire('Durant', 400000)
    c1.depot(1000)
    c1.affiche()

    c2 = Compte_bancaire()
    c2.retrait(500)
    c2.affiche()
