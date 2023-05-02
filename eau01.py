""" Combinaison de 2 nombres """

# Créer un programme qui affiche toutes les différentes combinaisons de 2 nombres entre 00 et 99 dans l'ordre croissant.

"ce truc n'a ni queue ni tête !"

leftCount = 0
rightCount = 0
display = (" %d  %d " % (leftCount, rightCount))


while leftCount <= 99 and rightCount <= 99:
    
    rightCount += 1
    
    if rightCount == 99 and leftCount < 99:
        leftCount += 1
        rightCount = 0
        print(display)
        continue
    
    if leftCount == 99 and rightCount == 99:
        print("you have reached 99  99 and the end of the given possibility")
        break
    
    else:
        continue

print(display)