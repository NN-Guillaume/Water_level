""" Chiffres only """

# Créer un programme qui détermine si une chaîne de caractère ne contient que des chiffres.
# Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


# Evaluate if int or not in string
def is_int_or_not(arg):
    isInteger = True

    try:
        int(arg)
    except ValueError:
        isInteger = False
    
    if isInteger:
        print(" True ")
    else:
        print(" False ")


try:
    myTesting = str(sys.argv[1])
except:
    sys.exit(" ERROR ")


is_int_or_not(myTesting)


