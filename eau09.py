""" Entre min et max """

# Créer un programme qui affihe toutes les valeurs comprises entre 2 nombres, dans l'ordre croissant.
# Min INCLUS
# Max EXCLUS
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments
#exemple ---> 20 25             display --->  20  21  22  23  24

import sys

try:
    input01 = int(sys.argv[1])
    input02 = int(sys.argv[2])
except:
    sys.exit(" ERROR ")

if input01 <= input02:
    minVal = input01
    xElements = input02 - input01
elif input01 >= input02:
    minVal = input02
    xElements = input01 - input02
else:
    print(" unexpected error ")

myList = []

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
