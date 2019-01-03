# Afficher une table de conversion de sommes d'argent exprimées en euros, en dollars américains.
# La progression des sommes de la tables sera géométrique :
# 1 euro(s) = 1.65 dollar(s)
# 2 euro(s) = 3.30 dollar(s)
# 4 euro(s) = 6.60 dollar(s)
# 8 euro(s) = 13.20 dollar(s)
# etc. S'arrêter à 16 384 euros

money_euro = money_dollar = 1
while money_euro <= 16384:
    money_dollar = money_euro * 1.65
    print(money_euro, " euro(s) = ", money_dollar, " dollar(s)")
    money_euro = money_euro * 2