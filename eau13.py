""" Tri par sélection """

# Créer un programme qui trie une liste de nombres.
# implémentation du tri par sélection OBLIGATOIRE.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

# voir sur Wikimerdia... ou pas !

import sys

try:
    # exemple of use --->       "5 3 1 4 2"
    testInput = str(sys.argv[1])
    # this below turn the string of numbers into a list of integers INSTEAD OF a list of string numbers
    listToOrdo = list(map(int, testInput.split()))
except:
    sys.exit(" ERROR ")

def selectionSort(list):
    for num in range(len(list)):
        minNum = num
        for i in range(num, len(list)):
            print(list)
            if list[i] < list[minNum]:
                minNum = i
        list[num], list[minNum] = list[minNum], list[num]
    
    return list

selectionSort(listToOrdo)
print(listToOrdo)
