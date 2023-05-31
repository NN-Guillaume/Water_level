""" Paramètres à l'envers """

# Créer un programme qui affiche ses arguments reçus à l'envers.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


try:
    arguments = str(sys.argv[1]) # exemple --->     "1000 milliards de 1000 millions de 1000 sabords !"
    list_args = arguments.rsplit(" ")
    reverse_list = (list_args[::-1])
    print(*reverse_list, sep='\n')
    
    # the code below convert into a string and print in reverse on a single line
    #displayStr = " ".join(reverseList) 
    #print(displayStr) # print the arguments but in reverse


except:
    print(" ERROR ")
    sys.exit(" EXIT ")