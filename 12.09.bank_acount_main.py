""" Écrivez un nouveau script qui récupère le code de l’exercice 12.2 (compte bancaire) en l’important comme un module. Définissez-y une nouvelle 
classe CompteEpargne(), dérivant de la classe CompteBancaire() importée, qui permette de créer des comptes d’épargne rapportant un certain intérêt 
au cours du temps. Pour simplifier, nous admettrons que ces intérêts sont calculés tous les mois. Le constructeur de votre nouvelle classe 
devra initialiser un taux d’intérêt mensuel par défaut égal à 0,3 %. Une méthode changeTaux(valeur) devra permettre de modifier ce taux à volonté.
Une méthode capitalisation(nombreMois) devra :
• afficher le nombre de mois et le taux d’intérêt pris en compte ;
• calculer le solde atteint en capitalisant les intérêts composés, pour le taux et le
nombre de mois qui auront été choisis.
Exemple d’utilisation de la nouvelle classe :
    c1 = CompteEpargne('Duvivier', 600)
    c1.depot(350)
    c1.affiche()
Le solde du compte bancaire de Duvivier est de 950 euros.
    c1.capitalisation(12)
Capitalisation sur 12 mois au taux mensuel de 0.3 %.
    c1.affiche()
Le solde du compte bancaire de Duvivier est de 984.769981274 euros.
    c1.changeTaux(.5)
    c1.capitalisation(12)
Capitalisation sur 12 mois au taux mensuel de 0.5 %.
    c1.affiche()
Le solde du compte bancaire de Duvivier est de 1045.50843891 euros. """


from bank_acount import Compte_bancaire

class Compte_epargne(Compte_bancaire):
    "Définition de la classe Compte_epargne qui hérite de la classe Compte_bancaire, en y rajoutant les intérêts"

    def __init__(self, nom = 'Gates', solde = '100000000000'):
        "Constructeur de la classe Compte_épargne définissant le taux d'intérêt"
        Compte_bancaire.__init__(self, nom, solde)
        self.taux = 0.3

    def change_taux(self, interet):
        "Méthode modifiant le taux d'intérêt"
        self.taux = interet

    def capitalisation(self, nb_mois):
        "Méthode retournant le montant de l'épargne calculée avec les intérêts"
        self.solde = self.solde * (1+self.taux/100)**nb_mois
        print("Le nombre de mois pris en compte est de {} pour un taux d’intérêt de {}%".format(nb_mois, self.taux))
        print("Le solde atteint en capitalisant les intérêts composés est de {:.2f} euros\n".format(self.solde))


if __name__ == "__main__":
    c1 = Compte_epargne('Duvivier', 600)
    c1.depot(350)
    c1.affiche()

    c1.capitalisation(12)
    c1.affiche()

    c1.change_taux(.5)
    c1.capitalisation(12)
    c1.affiche()