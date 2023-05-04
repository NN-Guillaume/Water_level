""" Différence minimum absolue """

# Créer un programme qui affihe la différence minimum absolue entre 2 éléments d'un tableau constitué uniquement de nombres.
# Nombres négatifs acceptés
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

import sys

try:
    # exemple of use --->       "10 6 5 9 48"
    testInput = str(sys.argv[1])
    # this below turn the string of numbers into a list of integers INSTEAD OF a list of string numbers
    testList = list(map(int, testInput.split()))
except:
    sys.exit(" ERROR ")

newList = []

# Put all the numbers in order, according to upper exemple ---> [5, 6, 9, 10, 48]
def sortList(arglist):
    arglist.sort()
    #print(arglist)

# Got the value by substracting number n+1 by n, according to upper exemple ---> [1, 3, 1, 38, 48]
def getInterValues(arglist):
    sortList(arglist)
    index = int
    elem = int
    for index, elem in enumerate(arglist):
        if(index<(len(arglist)-1)):        
            #newList.append(elem - arglist[index+1])
            newList.append(arglist[index+1] - elem)
        else:
            newList.append(elem)
    #print(newList)

# Remove the last position number and get the smallest value, according to upper exemple ---> [1, 3, 1, 38] ---> "1"
def getSmallest(newarg):
    newarg.pop(-1)
    fuckingMin = min(newarg)
    print(fuckingMin)

getInterValues(testList)
getSmallest(newList)
