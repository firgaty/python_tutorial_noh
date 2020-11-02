"""
Exemple pour le jeu "Trouve le nombre"
"""

import os
from random import randint 

def clear_terminal():
    """
    Efface le terminal
    """
    # Pas grand chose à en dire, faut lire la documentation 
    # pour savoir ça (ou faire un recherche en ligne), rien 
    # qui ne soir nécessaire pour le moment.
    os.system('cls' if os.name == 'nt' else 'clear')

def to_integer(s, a, b):
    """
    Détermine si la chaîne s est un entier entre a et b, a < b.
    Renvoie None si ce n'est pas un entier, sinon un entier
    
    Arguments:
    s -- Chaîne à analyser et caster
    a -- Minimum
    b -- Maximum 
    """
        
    # Check si c'est un entier
    if not s.isdigit():
        return None # C'en n'est pas un.
    
    # Comme l'entrée représente un entier positif, on peut le "caster" en int.
    s = int(s)
    
    # On test si l'entrée est entre a et b:
    if s < a or s > b:
        # Ce n'est pas un entier entre a et b.
        return None # Il n'est pas dedans

    return s

def get_input(a, b):
    """
    Renvoie l'input correct de l'utilisateur sous forme d'entier (int).

    Arguments:
    a -- Le minimum attendu, a > 0
    b -- Le maximum attendu, b > a
    """
    
    # Boucle infinie tant que l'on a pas le résultat escompté.
    while True:
        print("Entrez un nombre entre {} et {}:".format(a, b))
        
        # On récupère l'entrée utilisateur.
        user_input = input()
        
        # On essaie de la caster en entier positif
        user_input = to_integer(user_input, a, b)
        
        if user_input is None:
            print("Ce n'est pas un nombre entier compris entre {} et {}...".format(a, b))
        else:
            # Le test précédent nous indique que 
            # l'entrée utilisateur correspond à nos attentes
            return user_input
    
def get_yes_no():
    """
    Renvoie la réponse à une question OUI/NON sous forme de booléen (bool)
    """
    
    # Boucle infinie: Tant que la réponse ne convient pas...
    while True:
        # On récupère l'input
        user_input = input("O|N: ")
        
        # Si ça correspond à un caractère pour "OUI"
        if user_input in ["o", "O", "y", "Y"]:
            return True
        # Si ça correspond à un caractère pour "NON"
        if user_input in ['n', 'N']:
            return False
        # Sinon on n'arrête pas la boucle

def game_loop(a, b):
    """
    Joue une partie de "Trouver le nombre entre a et b".
    """
    # On génère un entier entre a et b, le 'secret'.
    secret = randint(a, b)
    counter = 0 # Initialisation le compteur de tentatives.
    
    # Boucle de jeux, se termine quand la réponse est trouvée.
    while True:
        counter += 1 # On incrémente le nombre d'essais.
        user_input = get_input(a, b) # On récupère l'entrée utilisateur.
        
        if user_input == secret:  # Si l'entrée est le même nombre que le secret.
            break # On 'Casse' la boucle
        if user_input < secret: # Si plus petit que le secret.
            print("C'est plus!")
        else: # Sinon c'est plus grand...
            print("C'est moins!")
    
    clear_terminal()
    # On est sortis de la boucle, donc c'est gagné.
    print("Vous avez GAGNÉ !\n")
    # On imprime les stats
    print("Nombre secret: {}\nNombre d'essais: {}\n".format(secret, counter))

def menu_loop():
    levels=[10, 100, 1000]
    
    # On stock la longueur de la liste de niveaux pour éviter
    # d'avoir à rappeler la fonction len()
    l = len(levels)
    user_input = 0 # Initialisation de l'entrée utilisateur
    
    # Boucle infinie tant que le PROGRAMME n'est pas fini 
    # (Il peut y avoir plusieurs parties)
    while True:
        clear_terminal()
        print("Choix du niveau:")
        
        # On affiche tous les niveaux et le numéro leur correspondant
        for i in range(l):
            print("{}) De 0 à {}".format(i + 1, levels[i]))
            
        # On récupère l'entrée utilisateur
        user_input = get_input(1, l)
        clear_terminal()
        
        # On lance le jeu
        game_loop(0, levels[user_input - 1])
        
        # La partie est terminer, on vérifie que le joueur
        # Veut continuer ou quitter
        print("Voulez vous rejouer ?")
        if not get_yes_no():
            # On quitte
            clear_terminal()
            print("Bye ~")
            break # Fin de la boucle principale


# On lance le menu principal.
menu_loop()


        