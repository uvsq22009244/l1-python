def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return (((temps[0] * 24) + temps[1])*60 + temps[2])*60 + temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    minute = seconde // 60
    seconde %= 60
    heure = minute // 60
    minute %= 60
    jour = heure // 24
    heure %= 24
    return (jour, heure, minute, seconde)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


def afficheTemps(temps):
    return(jour, heure, minute, seconde)
    
afficheTemps((1,0,14,23))    
print(afficheTemps[0],"jours", afficheTemps[1], "heures", afficheTemps[2], "minutes", afficheTemps[3], "secondes")