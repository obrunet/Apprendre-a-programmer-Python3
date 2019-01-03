# Dans un conte américain, huit petits canetons s’appellent respectivement : Jack, Kack, Lack, Mack, Nack, Oack, Pack et Qack. 
# Écrivez un petit script qui génère tous ces noms à partir des deux chaînes suivantes : 
# prefixes = 'JKLMNOP' et suffixe = 'ack' 
# Si vous utilisez une instruction for ... in ..., votre script ne devrait comporter que deux lignes. 

prefix, suffix = "JKLMNOP",  "ack"

for car in prefix:
    print(car+suffix)




### other tests for me :)

animalsList = [ "dog", "cat", "tiger", "mouse"]
for animal in animalsList:
    print("Length of the string:", animal, ":", len(animal))

miscList = [ "a string", 12, 12.5, 'z']
for elt in miscList:
    print("Type of element:", type(elt))