# Converti en radians un angle fourni au départ en degrés, minutes, secondes

angle_deg, angle_min, angle_sec = 45, 25, 52

fm = angle_sec / 60             # sec. -> fraction of min.
fd = (angle_min + fm) / 60      # min. -> fraction of deg.
angle = angle_deg + fd          # angle in deg

angle_rad = angle * (3.14159 / 180)

print(angle_deg, "°", angle_min, "'", angle_sec, "'' = ", angle, "deg =", angle_rad, "rad.")