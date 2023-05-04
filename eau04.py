""" Prochain nombre premier """

# Créer un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.
# Affiche -1 si le paramètre est négatif OU mauvais

import sys

# will calculate the next Prime number even if the input is not a Prime number
def nextPrimeAnyway(n):

    newVal = n

    while not isPrimeNumber(newVal):

        #print("newVal is equal to %d" % (newVal))
        newVal += 1

        if isPrimeNumber(newVal):
            #print(" proof of access #1 ")
            print(newVal)
            break

        else:
            continue

# will calculate the next Prime number IF the input is a Prime number
def nextPrime(n):

    newVal = myNum + 1

    if isPrimeNumber(n): #si il s'agit bien d'un nombre premier
        
        while not isPrimeNumber(newVal):

            #print("newVal is equal to %d" % (newVal))
            newVal += 1

            if isPrimeNumber(newVal):
                #print(" proof of access #1 ")
                print(newVal)

            else:
                continue

    else: #si ce n'est PAS un nombre premier
        print(" NOT prime ")

# Define if a digit/number is a prime one or not
def isPrimeNumber(myNum):
    try:

        #wrongResult = " %d n'est pas un nombre premier " % (myNum)
        #goodResult = " %d est un nombre premier " % (myNum)

        # 0 and 1 are NOT prime digits
        if myNum == 0 or myNum == 1:
            #print(wrongResult)
            return False

        # 2, 3, 5 and 7 ARE prime digits
        elif myNum == 2 or myNum == 3 or myNum == 5 or myNum == 7:
            #print(goodResult)
            return True

        # # if last digit is a number dividing by 2 then it is NOT prime
        elif ((myNum % 2 == 0) or (myNum % 2 == 2) or (myNum % 2 == 4) or (myNum % 2 == 5) or (myNum % 2 == 6) or (myNum % 2 == 8)):
            #print(wrongResult)
            return False

        # if last digit is a number dividing by 3 then it is NOT prime
        elif ((myNum % 3 == 0) or (myNum % 3 == 3) or (myNum % 3 == 6) or (myNum % 3 == 9)):
            #print(wrongResult)
            return False

        # if last digit is a number dividing by 4 then it is NOT prime
        elif ((myNum % 4 == 0) or (myNum % 4 == 2) or (myNum % 4 == 4) or (myNum % 4 == 5) or (myNum % 4 == 6) or (myNum % 4 == 8)):
            #print(wrongResult)
            return False

        # if last digit is a number dividing by 5 then it is NOT prime
        elif (myNum % 5 == 0) or (myNum % 5 == 5):
            #print(wrongResult)
            return False

        # after all the verifications above, the rest can be only a prime number
        else:
            #print(goodResult)
            return True

    except ValueError:
        print(" -1 ")

try:
    myNum = int(sys.argv[1])
except:
    sys.exit(" -1 ")

nextPrimeAnyway(myNum)
