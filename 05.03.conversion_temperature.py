# converti température degré Fahrenheit <-> degré Celsius
# Tf = Tc x 1.8 + 32

Tc = 37.8
Tf = Tc*1.8+32
print("The temperature in Celsius is equal to", Tc, "\n","The equivalent temperature in Fahrenheit is equal to", int(Tf))

nTc = (Tf-32)/1.8
print("2nd conversion back in celsius: ", nTc)