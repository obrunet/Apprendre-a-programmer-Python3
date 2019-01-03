# Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie par l’utilisateur en miles/heure. 
# (Rappel : 1 mile = 1609 mètres) 

Speedmph = 0
while (Speedmph <= 0): # or (type(Speedmph) != int):
    print("Enter a speed in miles per hour (integer > 0):")
    Speedmph = int(input())

Speedkmh = Speedmph*1609/1000
Speedms = Speedkmh*1000/3600

print("This speed is equal to", Speedms, "m/s =", Speedkmh, "km/h")
