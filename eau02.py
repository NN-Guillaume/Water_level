""" Paramètres à l'envers """

# Créer un programme qui affiche ses arguments reçus à l'envers.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys

try:
    arguments = str(sys.argv[1]) # exemple --->     "1000 milliards de 1000 millions de 1000 sabords !"
    listArgs = arguments.rsplit(" ") 

    print(listArgs[::-1]) # print the whole list/array but in reverse
except ValueError:
    print("ERROR")
    # write a command to quit the program