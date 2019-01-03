# Converti en degrés, minutes, seconds un angle fourni au départ en radians
# Rad =  Deg ∗ π / 180

angle_rad = 0.7929218019753086
angle_deg = angle_rad * 180 / 3.14159

dDeg = int(angle_deg)                           # nbre de degré = partie entière

decimal = (angle_deg - dDeg)                    # partie décimale
fraction = decimal * 3600                            # convertie en sec

dMin = fraction // 60                           # calcule nbre minutes -> div. entière
dSec = fraction - dMin * 60                     # reste = sec

print(angle_rad, "rad. =", angle_deg, "deg. = ", dDeg, "°", int(dMin), "'", int(dSec), "''")    # dSec mériterait d'être arrondi...