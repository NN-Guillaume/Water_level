""" Prochain nombre premier """

# Créer un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.
# Affiche -1 si le paramètre est négatif OU mauvais

import sys


try:

    """ Describe function """
    def newPrime(myNum):
        
        print("proof of access")
        
        upperValue = myNum + 1
        while mathPrime(upperValue) != isPrime:
            upperValue+=1
            if mathPrime(upperValue) == isPrime:
                print("congrats")
                print(upperValue)
            else:
                continue





    """ If prime number then look for the next one """
    def confirmIsPrime(isPrime):
        # simple verif for now
        if isPrime == True:
            print("PRIME NUMBER !")
            #print(nbersList)
            
            #####################################
            # WORKS but display 1
            """basePrime = isPrime
            nextPrime = 0
            
            while nextPrime != isPrime:
                nextPrime+=1
                if nextPrime == isPrime:
                    print("congrats")
                    print(nextPrime)
                else:
                    continue"""
            
            #####################################
            """upperValue = myNum + 1
            while mathPrime(upperValue) != isPrime:
                upperValue+=1
                if mathPrime(upperValue) == isPrime:
                    print("congrats")
                    print(upperValue)
                else:
                    continue"""
            
            #####################################
            
            upperValue = myNum + 1
            print(" connerie de merde !")
            while mathPrime(upperValue) != mathPrime(isPrime):
                upperValue+=1
            if mathPrime(upperValue) == mathPrime(isPrime):
                print("congrats")
                print(upperValue)
                
            else:
                pass
            #####################################

            #newPrime(isPrime)

        elif isPrime == False:
            print("NOT a prime number !")
            #print(nbersList)
        else:
            print(" I am tired of this shit ")




    """ Define if a digit/number is a prime one or not   +  other function ? """
    def mathPrime(myNum):
        try:
            #myNum = int(sys.argv[1])

            # 0 and 1 are NOT prime digits
            if myNum == 0 or myNum == 1:
                resultat = "%d n'est pas un nombre entier !" % (myNum)
                print(resultat)
                isPrime = False

            # 2, 3, 5 and 7 ARE prime digits
            elif myNum == 2 or myNum == 3 or myNum == 5 or myNum == 7:
                resultat = "%d est bien un nombre entier !" % (myNum)
                print(resultat)
                isPrime = True

            # # if last digit is a number dividing by 2 then it is NOT prime
            elif ((myNum % 2 == 0) or (myNum % 2 == 2) or (myNum % 2 == 4) or (myNum % 2 == 5) or (myNum % 2 == 6) or (myNum % 2 == 8)):
                resultat = "%d n'est pas un nombre entier !" % (myNum)
                print(resultat)
                isPrime = False

            # if last digit is a number dividing by 3 then it is NOT prime
            elif ((myNum % 3 == 0) or (myNum % 3 == 3) or (myNum % 3 == 6) or (myNum % 3 == 9)):
                resultat = "%d n'est pas un nombre entier !" % (myNum)
                print(resultat)
                isPrime = False

            # if last digit is a number dividing by 4 then it is NOT prime
            elif ((myNum % 4 == 0) or (myNum % 4 == 2) or (myNum % 4 == 4) or (myNum % 4 == 5) or (myNum % 4 == 6) or (myNum % 4 == 8)):
                resultat = "%d n'est pas un nombre entier !" % (myNum)
                print(resultat)
                isPrime = False

            # if last digit is a number dividing by 5 then it is NOT prime
            elif (myNum % 5 == 0) or (myNum % 5 == 5):
                resultat = "%d n'est pas un nombre entier !" % (myNum)
                print(resultat)
                isPrime = False

            else:
                resultat = " YES ! %d est bien un nombre entier !" % (myNum)
                print(resultat)
                isPrime = True

            #CALL FUNCTION HERE !
            confirmIsPrime(isPrime)

        except ValueError:
            print("Never trust the user !!!")
            #loop = False

    """ Increment by 1 the last number of a list """
    def incrementList():
        end_pos = nbersList[-1]
        #end_pos = 0
        upValue = end_pos + 1
        nbersList.append(upValue)

    """ Allow to add new values inside the list according to the user input """
    def listAdd(myNum):
        while myNum != nbersList[-1]:
            incrementList()
            if myNum == nbersList[-1]:
                print("success")
            elif myNum == nbersList[myNum]:
                print("exists")
            else:
                continue


    myNum = int(sys.argv[1])
    #nbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nextPrime = 0
    isPrime = bool
    #listAdd(myNum)
    mathPrime(myNum)
    #newPrime(myNum)

except ValueError:
    print("-1")
