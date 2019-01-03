# Convertir un nombre entier de secondes fourni au départ en un nombre d'années , de mois, de jours, de minutes et de secondes

nbTime =  1567432                       # choosen nb of time in seconds - tested with 50/60/70/60*60/24*60*60/12*30*24*60*60/  etc...

remSec = nbTime                         # the remaining seconds after calculation

nbYears = remSec // (12*30*24*60*60)              # nb of sec in 1 year
remSec = remSec %   (12*30*24*60*60)

nbMonths = remSec //   (30*24*60*60)              # nb of sec in 1 month
remSec = remSec %      (30*24*60*60)

nbDays = remSec //        (24*60*60)              # nb of sec in 1 day
remSec =  remSec %        (24*60*60)

nbHours = remSec //          (60*60)              # nb of sec in 1 hour
remSec =  remSec %           (60*60)

nbMin = remSec //               (60)              # nb of sec in 1 day
nbSec =  remSec %               (60)

print(nbYears,"year(s),", nbMonths, "month(s),", nbDays, "day(s),", nbHours, "hour(s),", nbMin, "minute(s),", nbSec, "second(s).")





### previous buggy version :
"""
nbSeconds = nbMinutes = nbHours = nbDays = nbMonths = nbYears = 0

nbSeconds = nbTime % 60
if nbTime >= 60:                                    # more than 1 min
    nbMinutes = nbTime // 60
if nbTime >= 60*60:                                 # more than 1 hour
    nbHours = nbTime // (60*60)
    nbMinutes = nbTime % (60*60)
if nbTime >= (24*60*60):                            # more than 1 day
    nbDays = nbTime // (24*60*60)
    nbHours = nbTime % (24*60*60)
if nbTime >= (30*24*60*60):                         # more than 1 month
    nbMonths = nbTime // (30*24*60*60)
    nbDays = nbTime % (30*24*60*60)
if nbTime >= (12*30*24*60*60):                      # more than 1 year
    nbYears = nbTime // (12*30*24*60*60)
    nbMonths = nbTime % (12*30*24*60*60)


if nbTime < (60*60):
    nbMinutes = nbTime % (60*60)
    if nbTime < (60*60*24):  
        nbHours = nbTime % (60*60*24) 
        if nbTime < (60*60*24*30):
            nbDays = nbTime % (60*60*24*30)
            if nbTime < (60*60*24*30*365):
                nbMonths = nbTime % (60*60*24*30*365)
                if nbTime < (60*60*24*30*365):
                    nbYears = nbTime // (60*60*24*30*365)
                    """