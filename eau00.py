""" Combinaison de 3 chiffres """

# Créer un programme qui affiche toutes les différentes combinaisons possibles de 3 chiffres dans l'ordre croissant
#                                                                                                           dans l'ordre croissant.
#                                                                                                           répétition volontaire ( WTF ??? )

import sys

numList = []

def removeDouble(arglist):
    for x in arglist:
        #if numList[0] == numList[1] or numList[1] == numList[2] or numList[0] == numList[2]:
        if arglist[0] == arglist[1] == arglist[2]:
            print(" double detected ! ")
            arglist.remove(x)
            print(arglist)

"""def removeDouble(i, j, k):
    for i, j, k in numList:
        if numList[i] == numList[j] or numList[j] == numList[k] or numList[i] == numList[k]:
            print(" double detected ! ")
            numList.remove(i, j, k)"""

def generateNum():
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                numList = [i,j,k]
                removeDouble(numList)
                #print(numList)

generateNum()
removeDouble()
#print(numList)

# trier les "doublons"

# transformer en nombre normaux pour présentation du résultat final
# ', '.join(str(e) for e in numList)

#print(numList)