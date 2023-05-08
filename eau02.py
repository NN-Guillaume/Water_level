""" Paramètres à l'envers """

# Créer un programme qui affiche ses arguments reçus à l'envers.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys

try:
    arguments = str(sys.argv[1]) # exemple --->     "1000 milliards de 1000 millions de 1000 sabords !"
    listArgs = arguments.rsplit(" ")
    reverseList = (listArgs[::-1])
    displayStr = " ".join(reverseList) 
    print(displayStr) # print the arguments but in reverse

except:
    print(" ERROR ")
    sys.exit(" EXIT ")