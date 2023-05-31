""" Combinaison de 2 nombres """

# Créer un programme qui affiche toutes les différentes combinaisons de 2 nombres entre 00 et 99 dans l'ordre croissant.

def display_two_numbers():
    for i in range(100):
        for j in range(i, 100):
            print(f"{i:02d}{j:02d}", end=", ")

display_two_numbers()