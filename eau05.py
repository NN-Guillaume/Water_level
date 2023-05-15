""" String dans string """

# Créer un programme qui détermine si une chaîne de caractères se trouve dans un autre.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys


# turn the string into a list
def splitArgv(string):
    return list(string)


# verify the elements in common, works even if not attached to each others
def sameElem(arg1, arg2):
    for x in arg1:
        for y in arg2:
            if x == y:
                verdict = True
                #print("TRUE")
                return verdict


def atStartOrAtEnd(arg1, arg2):
    if arg1[-1:] == arg2[-1:]: # good ! check the end
        print("True")
    elif arg1[:+1] == arg2[:+1]: # good ! check the begining
        print("True")
    elif sameElem(arg1, arg2):
        print("Contain identical letters but in disorder")
    elif not sameElem(arg1, arg2):
        print("False")
    else:
        print("unexpected event")


try:
    input01 = str(sys.argv[1]) # Bonjour
    input02 = str(sys.argv[2]) # jour
except:
    sys.exit(" ERROR ")


# print(splitArgv(input01))
splitArgv(input01)
# print(splitArgv(input02))
splitArgv(input02)

atStartOrAtEnd(input01, input02)