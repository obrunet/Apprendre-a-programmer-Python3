# Écrivez une fonction chaineListe() qui convertisse une phrase en une liste de mots. 

# My solution
def chainList(sent):
    i, j = 0, 0                             # i = parsing index / j = index of the begining of the word
    wordList = []
    while i<len(sent):
        if sent[i] == " ":
            wordList.append(sent[j:i])
            j = i+1
        if i == (len(sent)-1):              # add the last word not followed by a space
            wordList.append(sent[j:i+1])
        i += 1
    return wordList

if __name__ == "__main__":
    userSentence = "This is an example of a sentence"
    print(chainList(userSentence))

 



# Answer of the book, which is quite different
def chaineListe(ch):     
    "convertit la chaîne ch en une liste de mots"     
    liste, ct = [], ""          # ct est une chaîne temporaire     
    for c in ch:                # examiner tous les caractères de ch         
        if c == " ":            # lorsqu'on rencontre un espace,             
            liste.append(ct)    # on ajoute la chaîne temporaire à la liste             
            ct = ""             # ... et on ré-initialise la chaîne temporaire         
        else:                   # les autres caractères examinés sont ajoutés à la chaîne temp. :             
            ct = ct + c         # Ne pas oublier le mot restant après le dernier espace ! :          
    if ct:                      # vérifier si ct n'est pas une chaîne vide         
        liste.append(ct)     
    return liste                # renvoyer la liste ainsi construite 

# Tests : 
if __name__ == '__main__':     
    li = chaineListe("René est un")     
    print(li)     
    for mot in li:         
        print(mot, "-", end=' ')     
    print(chaineListe(""))              # doit renvoyer une liste vide 