# Un nombre premier est un nombre qui n’est divisible que par un et par lui-même. Écrivez un
# programme qui établit la liste de tous les nombres premiers compris entre 1 et 1000,
# en utilisant la méthode du crible d’Eratosthène :
# • Créez une liste de 1000 éléments, chacun initialisé à la valeur 1.
# • Parcourez cette liste à partir de l’élément d’indice 2 : si l’élément analysé possède la
# valeur 1, mettez à zéro tous les autres éléments de la liste, dont les indices sont des
# multiples entiers de l’indice auquel vous êtes arrivé.
# Lorsque vous aurez parcouru ainsi toute la liste, les indices des éléments qui seront
# restés à 1 seront les nombres premiers recherchés.
# En effet : A partir de l’indice 2, vous annulez tous les éléments d’indices pairs : 4, 6, 8,
# 10, etc. Avec l’indice 3, vous annulez les éléments d’indices 6, 9, 12, 15, etc., et ainsi de
# suite. Seuls resteront à 1 les éléments dont les indices sont effectivement des nombres
# premiers.

prime_list = [1] * 1000

for i in range (2, 1000):
    for j in range (i*2, 1000, i):      # tous les élts à l'index j = multiple de i
        prime_list[j] = 0               # sont mis à 0

for i in range (1, 1000):
    if prime_list[i]:
        print(i, end=" ")               # affiche les indices des nbres != 0