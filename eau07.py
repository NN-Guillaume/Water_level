""" Majuscule """

# Créer un programme qui met en majuscule la 1-ière lettre de chaque mot dans une chaîne de caractère.
# Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


# manage the letters transformation
def upper_first_letter(arg):
    count = 0
    for i in arg:

        if i == " ":
            manage_blank(i)
            count = 0

        else:
            count += 1
            if count == 1:
                upper_case(i)
            elif count >= 1:
                lower_case(i)


# put back the space at their right place
def manage_blank(blankCase):
    blankCase = " "
    print(blankCase, end=' ')


# transform to uppercase
def upper_case(arg):
    upCase = arg.upper()
    print(upCase, end=' ')


# transform to lowercase
def lower_case(arg):
    lowCase = arg.lower()
    print(lowCase, end=' ')


try:
    myStr = str(sys.argv[1]) # "hello my dude, how are you doing ?"  Hello My Dude, How Are You Doing ?"
except IndexError:
    sys.exit(" ERROR ")


upper_first_letter(myStr)
