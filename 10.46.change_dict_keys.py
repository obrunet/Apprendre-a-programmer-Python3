# Écrivez une fonction qui échange les clés et les valeurs d’un dictionnaire 
# (ce qui permettra par exemple de transformer un dictionnaire anglais/français en un dictionnaire français/anglais). 
# On suppose que le dictionnaire ne contient pas plusieurs valeurs identiques. 

translation_dic = {
    'souris': 'mouse',
    'clavier': 'keyboard',
    'ecran': 'screen',
    'portable': 'laptop',
    'ordinateur de bureau': 'desktop',
    'serveur': 'server',
    'site internet': 'web site'
}

print(translation_dic, "\n")

inverted_dic = {}
for k, val in translation_dic.items():
    inverted_dic[val] = k

print(inverted_dic)