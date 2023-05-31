""" Entre min et max """

# Créer un programme qui affihe toutes les valeurs comprises entre 2 nombres, dans l'ordre croissant.
# Min INCLUS
# Max EXCLUS
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments
#exemple ---> 20 25             display --->  20  21  22  23  24

import sys


def from_min_to_max_minus_1(val1, val2):
    
    myList = []
    
    if val1 <= val2:
        minVal = val1
        xElements = val2 - val1
    elif val1 >= val2:
        minVal = val2
        xElements = val1 - val2
    else:
        print(" unexpected error ")
        return
    
    myList.append(minVal)


    while len(myList) <= xElements:
        lastPos = myList[-1]
        newVal  = lastPos + 1
        myList.append(newVal)
        
        if len(myList) == xElements:
            print(myList)
            break
        
        else:
            continue


try:
    input01 = int(sys.argv[1])
    input02 = int(sys.argv[2])
except:
    sys.exit(" ERROR ")


from_min_to_max_minus_1(input01, input02)