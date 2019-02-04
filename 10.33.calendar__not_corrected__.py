# Écrivez un script capable d’afficher la liste de tous les jours d’une année imaginaire, laquelle commencerait un jeudi. 
# Votre script utilisera lui-même trois listes : 
# une liste des noms de jours de la semaine, 
# une liste des noms des mois, 
# et une liste des nombres de jours que comportent chacun des mois (ne pas tenir compte des années bissextiles). 
# Exemple de sortie : jeudi 1 janvier   vendredi 2 janvier   samedi 3 janvier   dimanche 4 janvier ... et ainsi de suite, jusqu’au jeudi 31 décembre.

week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
year_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
month_nb_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_idx, month_idx, month_day_idx = 1, 1, 1
"""
print(6%7)
print(7%7)
print(8%7)
print(9%7)
"""
for i in range (1, 366):    

    if month_day_idx > month_nb_days[month_idx-1]:        # change of month
        month_idx += 1
        month_day_idx = 1
        print("\n\n")

    day_idx = (i + 3) % 7
    result = "day #{}:{} {} {}   -   "  # for instance = day #2 friday 02 january 
    print(result.format(i, week_days[day_idx-1], month_day_idx, year_months[month_idx-1]), end="")

    month_day_idx += 1


