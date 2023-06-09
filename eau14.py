""" Par ordre Ascii """

# Créer un programme qui trie les éléments donnés en argument par ordre ASCII.
# Afficher "ERROR" et quitter le programme en cas de problèmes d'arguments

# python already knows about numerical AND alphabetical order  ;-)
#result = "A"<"B"
#print(result) # True

import sys


def return_to_string(li):
    simpleStr = ' '.join(map(str, li))
    print(simpleStr, end=' ')


def bubble_sort(list):
    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage = passage+1
        for i in range(0, len(list)- passage):
            #print(list)
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                permutation = True
    
    return list


try:
    # exemple of use --->       "Opel Mercedes-Benz BMW Lamborghini Bugatti"   or  "A Z E R T Y"
    testInput = str(sys.argv[1])
    listToOrdo = list(testInput.split(" "))
    #print(listToOrdo)
except:
    sys.exit(" ERROR ")


bubble_sort(listToOrdo)
#print(listToOrdo)
return_to_string(listToOrdo)