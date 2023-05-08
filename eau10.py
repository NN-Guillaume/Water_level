""" Index wanted """

# Créer un programme qui affihe le premier index d'un élément recherché dans un tableau.
# Le tableau est constitué de TOUS les arguments à l'EXCEPTION du dernier.
# L'élément recherché est le DERNIER argument.
# Afficher -1 si l'élément n'est pas trouvé.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

# Exemple ---> "Macron is a fucking criminal who must die in a slow and painful way" "fucking"
#              stat of the list                                        end of list      fucking is the argument to look for
# "fucking" is in the third position ---> display ---> "3"

import sys

def getIndex(arg1, arg2):
    try:
        splitSent = arg1.rsplit(" ")    # try to write your own code instead of using "rsplit()"
        print(splitSent)
        result = splitSent.index(arg2)
        print(result)
    except:
        print(" -1 ") #print "-1" if arg2 do not match anything in arg1


try:
    sentence = str(sys.argv[1])
    lookFor = str(sys.argv[2])
except IndexError:
    sys.exit(" ERROR ")


getIndex(sentence, lookFor)
