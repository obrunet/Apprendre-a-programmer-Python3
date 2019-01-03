# Demander à l’utilisateur son nom et son sexe (M ou F). 
# En fonction de ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne. 


print("Enter your surname:", end=" ")
enteredName = str(input())

print("Enter your gender (M or F):",  end=" ")
enteredGender = str(input())

if enteredGender == "M":
    print("Dear Mister", enteredName)
elif enteredGender == "F":
    print("Dear Madam", enteredName)
else:
    print("your gender in unknown...")