""" Majuscule sur deux """

# Créer un programme qui met en majuscule 1 lettre sur 2 dans une chaîne de caractère.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


# manage the letters transformation
def upper1on2(arg):
    count = 0
    for i in arg:
        if i == " ":
            manageBlank(i)
        else:
            count += 1
            if count % 2 == 1:
                upperCase(i)
            elif count % 2 == 0:
                lowerCase(i)

# put back the space at their right place
def manageBlank(arg):
    #blankCase = arg.isspace()
    blankCase = " "
    print(blankCase, end=' ')

# transform to uppercase
def upperCase(arg):
    upCase = arg.upper()
    print(upCase, end=' ')

# transform to lowercase
def lowerCase(arg):
    lowCase = arg.lower()
    print(lowCase, end=' ')


try:
    myStr = str(sys.argv[1]) # "Hello World !"  must become  "HeLlO wOrLd !"
except ValueError:
    if sys.argv[1] == int:
        sys.exit(" ERROR ")


upper1on2(myStr)
