#chiffre et déchiffre avec une clef K
#(entier pris entre 0 et 25)

def chiffreCesar(clef, clair) :
    #ici on suppose que clair ne contient les clé
    """clef ets un entier compris entre (0 et 25)"""
    chiffre = ""
    for c in clair : #c est un caractère
        tmp = ord(c) + clef
        if (tmp > 90) :
            tmp = ord(c) - 26 + clef
        chiffre = chiffre + chr(tmp)
    return chiffre

def dechiffreCesar(clef, chiffre) :
    clair = ""
    for c in chiffre :
        tmp = ord(c) - clef
        if (tmp < 65) :
            tmp = ord(c) + 26 - clef
        clair += chr(tmp)
    return clair

def decrypterCesar(chiffre) :
    L = [0 for i in range(26)]
    for c in chiffre :
        L[ord(c) - 65] = L[ord(c) - 65] + 1
    ind_max = 0 #on cherche l''indice le plus fréquent
    for i in range(len(L)) : 
        if L[ind_max] < L[i] :
            ind_max = 1
    clef = (ind_max - 4) % 26
    return dechiffreCesar(clef, chiffre)

ch2= "MOMO"
print(decrypterCesar(ch2))
"""(ch = "MESSAGZ"
s = chiffreCesar(5,ch)
print(dechiffreCesar(5,s))
#ord() donnait le code ASCII + "3")"""

"""texte_clair = opent("clair.txt", "r")
contenu = texte_clair.readlines()
contenu2 = []
for s in contenu :
    s = chiffreCesar(5,s)
f = open("chiffre.txt", "w")
for s in contenu2 :
    f.write(s)
f.close()"""