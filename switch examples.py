def numbers_to_strings(argument): 
    switcher = { 
        0: "zero", 
        1: "one", 
        2: "two", 
    } 
    return switcher.get(argument, "nothing") 
  

if __name__ == "__main__": 
    argument=0
    print numbers_to_strings(argument) 


# ______________________________________________________________________________

# Contrôle du flux d’exécution à l’aide d’un dictionnaire

materiau = input("Choisissez le matériau : ")
if materiau == 'fer':
	fonctionA()
elif materiau == 'bois':
	fonctionC()
elif materiau == 'cuivre':
	fonctionB()
elif materiau == 'pierre':
	fonctionD()
elif ... etc ...


materiau = input("Choisissez le matériau : ")
dico = {
	'fer':fonctionA,
	'bois':fonctionC,
	'cuivre':fonctionB,
	'pierre':fonctionD,
	}
dico[materiau]()
#### OU ####
dico.get(materiau, fonctAutreParDefaut)()



# ______________________________________________________________________________

# Construction d’un histogramme à l’aide d’un dictionnaire


texte ="les saucisses et saucissons secs sont dans le saloir"
lettres ={}
for c in texte:
	lettres[c] =lettres.get(c, 0) + 1

print(lettres)
{'t': 2, 'u': 2, 'r': 1, 's': 14, 'n': 3, 'o': 3, 'l': 3, 'i': 3, 'd': 1, 'e': 5,
'c': 3, ' ': 8, 'a': 4}