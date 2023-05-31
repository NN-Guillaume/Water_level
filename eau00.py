""" Combinaison de 3 chiffres """

# Créer un programme qui affiche toutes les différentes combinaisons possibles de 3 chiffres dans l'ordre croissant.

def dislpay_number():
    for i in range(10):
        for j in range(i, 10):
            for k in range(j, 10):
                if i != j or i != k or j != k:
                    print(f"{i}{j}{k}", end=", ")

dislpay_number()