""" Majuscule sur deux """

# Créer un programme qui met en majuscule 1 lettre sur 2 dans une chaîne de caractère.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


# manage the letters transformation
def upper_1_on_2(arg):
    count = 0
    for i in arg:
        if i == " ":
            manage_blank(i)
        else:
            count += 1
            if count % 2 == 1:
                upper_case(i)
            elif count % 2 == 0:
                lower_case(i)


# put back the space at their right place
def manage_blank(blankCase):
    #blankCase = arg.isspace()
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
    myStr = str(sys.argv[1]) # "Hello World !"  must become  "HeLlO wOrLd !"
except IndexError:
    sys.exit(" ERROR ")


upper_1_on_2(myStr)
