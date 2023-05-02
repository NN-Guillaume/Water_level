""" Tri à bulle """

# Créer un programme qui trie une liste de nombres.
# implémentation du tri à bulle OBLIGATOIRE.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

# voir sur Wikimerdia... ou pas !

import sys

# exemple of use --->       "5 3 1 4 2"
testInput = str(sys.argv[1])
# this below turn the string of numbers into a list of integers INSTEAD OF a list of string numbers
listToOrdo = list(map(int, testInput.split()))

#listToOrdo = [6, 5, 10, 4, 7, 8, 3, 9, 2, 1]

def bubbleSort(list):
    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage = passage+1
        for i in range(0, len(list)- passage):
            print(list)
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                permutation = True
    
    return list

bubbleSort(listToOrdo)
print(listToOrdo)