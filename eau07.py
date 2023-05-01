""" Majuscule """

# Créer un programme qui met en majuscule la 1-ière lettre de chaque mot dans une chaîne de caractère.
# Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


# manage the letters transformation
def upper1on2(arg):
    count = 0
    for i in arg:
        
        if i == " " or i == "-":
            manageBlank(i)
            count = 0
            
        else:
            count += 1
            if count == 1:
                upperCase(i)
            elif count >= 0:
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
    myStr = str(sys.argv[1]) # "hello my dude, how are you doing ?"  Hello My Dude, How Are You Doing ?"
except ValueError:
    if sys.argv[1] == int:
        sys.exit(" ERROR ")


upper1on2(myStr)
