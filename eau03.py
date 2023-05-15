""" Suite de FIBONACCI """

# Créer un programme qui affiche le N-ième élément de la suite de FIBONACCI.
# (0, 1, 1, 2) ---> début de la suite.
# Le premier élément est à l'index 0.
# Affiche -1 si le paramètre est négatif OU mauvais

import sys


base = [0, 1, 1, 2]


#build a list by adding the last and before-last values together
def mathFibo ():
    end_nber = base[-1] # get the last element in the list
    before_end = base[-2] # get the before-last element in the list

    newValue = before_end + end_nber

    base.append(newValue)


try:
    indice = int(sys.argv[1])
except:
    sys.exit(" -1 ")


while indice != len(base)-1:
    mathFibo()
    if  indice == len(base)-1:
        print(base)
        print(" The index n°%d correspond to the value %d in the Fibonacci continuity" % (indice, base[-1]))
    else:
        continue

