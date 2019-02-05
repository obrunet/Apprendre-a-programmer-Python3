# Écrivez un script qui compte les occurrences de chacune des lettres de l’alphabet dans un texte 
# (on simplifiera le problème en ne tenant pas compte des lettres accentuées).

text = "sfqgkplvemlktgposjfgzmektpskAfpzkBrlpz^fsfCnblmqfpoirDzertyuiopsdfFghjklmxcvbnoiuytrelkjhgfdnbvcfghjvb"

car_dict = {}
for c in text:
    c = c.lower()     
    # car_dict[c] = car_dict.get(c, 0) + 1          # EQUIVALENT SOLUTION
    if c not in car_dict:
        car_dict[c] = 1
    else:
        car_dict[c] += 1

car_list = list(car_dict.items()) 
car_list.sort() 

print(car_list, "\n")

for car, freq in car_list:     
    print("Car {} : {} frequency(s).".format(car, freq))
