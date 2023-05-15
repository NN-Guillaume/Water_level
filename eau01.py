""" Combinaison de 2 nombres """

# Créer un programme qui affiche toutes les différentes combinaisons de 2 nombres entre 00 et 99 dans l'ordre croissant.

def goUp(leftArg, rightArg):

    display = (" %d  %d " % (leftArg, rightArg))

    while leftArg != 99 and rightArg != 99:

        if rightArg == 0 or rightArg <= 99:

            rightArg += 1
            print("R = %d" % (rightArg))

            if rightArg == 99 and leftArg <= 99:

                leftArg += 1
                rightArg = 0
                print("L = %d" % (leftArg))

                #print(display, end=' ') # FUCKING ENDLESS 0 ! ! !

        elif rightArg == 99 and leftArg == 99:
            print(" E N D ")
            break

        else:
            continue


leftCount = 0
rightCount = 0


goUp(leftCount, rightCount)