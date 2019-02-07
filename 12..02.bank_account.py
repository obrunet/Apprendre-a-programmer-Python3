# Définissez une classe CompteBancaire(), qui permette d’instancier des objets tels que compte1, compte2, etc. 
# Le constructeur de cette classe initialisera deux attributs d’instance nom et solde, avec les valeurs par défaut ’Dupont’ et 1000. 
# Trois autres méthodes seront définies : 
# • depot(somme) permettra d’ajouter une certaine somme au solde ; 
# • retrait(somme) permettra de retirer une certaine somme du solde ; 
# • affiche() permettra d’afficher le nom du titulaire et le solde de son compte. 
# Exemples d’utilisation de cette classe : 
# >>> compte1 = CompteBancaire('Duchmol', 800) 
# >>> compte1.depot(350) >>> compte1.retrait(200) 
# >>> compte1.affiche() Le solde du compte bancaire de Duchmol est de 950 euros. 
# >>> compte2 = CompteBancaire() 
# >>> compte2.depot(25) 
# >>> compte2.affiche() 
# Le solde du compte bancaire de Dupont est de 1025 euros.

class Bank_account(object):
    "Defines a bank account with the following methods: balance, deposit, withdrawal, display infos"
    def __init__(self, name = 'Dupont', balance = 1000):
        "Initialize an object"
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        "Adds a deposit to the account balance"
        self.balance += amount

    def withdrawal(self, amount):
        "Substracts a withdrawal to the account balance"
        self.balance -= amount

    def display_infos(self):
        "Displays informations of the bank account"
        print("Bank account informations: Name: {}, Balance: {}".format(self.name, self.balance))


if __name__ == "__main__":
    account_1 = Bank_account('Duchmol', 800)
    account_1.deposit(350)
    account_1.withdrawal(200)
    account_1.display_infos()
    account_2 = Bank_account()
    account_2.deposit(25)
    account_2.display_infos()