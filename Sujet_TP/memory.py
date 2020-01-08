import numpy as np
import random

"""
@author vcoindet
Jeu de memory
"""

Tabl = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f']

def melange_carte(Tab):
    for i in range(1, len(Tab)):
        # pick an element in Tab[:i+1] with which to exchange Tab[i]
        j = int(random.random() * (i+1))
        Tab[i], Tab[j] = Tab[k], Tab[i]
    return Tab

def carte_cache(Tab):   #TODO
    """
        TODO
        Doit créer une liste de même longueur que la liste renvoyés dans la question précédentes
    """


def choisir_cartes(Tab):
    c1 = int(input("Choisissez une carte : "))
    print(Tab[c1])
    c2 = int(input("Choisissez une deuxieme carte : "))
    while c1 == c2:
        print("Erreur, la deuxieme carte ne peut être la même que la premiere ! ")
        c2 = int(inpt("Veuillez choisir une deuxieme carte différente de la premiere : "))
    print(Tab[c])
    return [c1,c2]


def retourne_carte (c1, c2, Tab, Tab_cache):    #TODO
    """
        TODO
        doit retrouner les cartes dans la liste cachée
    """

def jouer(Tab):
    print("Bienvenue sur notre Jeu Memory, ci dessous voici les cartes mise en jeu. Il y en a 12")
    print(Tab)
    Tab = melange_carte(Tab)
    print("Maintenant je vais melanger les cartes et les retourner")
    
    Tab_cache =  carte_cache(Tab)
    print(Tab_cache)

    [c1, c2] = choisir_cartes(Tab)
    Tab_cache = retourne_carte(c1, c2, Tab, Tab_cache)
    print(Tab_cache)
    
    while 0 in Tab_cache:
        [c1, c2] = choisir_cartes(Tab)
        
        Tab_cache = retourne_carte(c1, c2, Tab, Tab_cache)
        
        print(Tab_cache)
        
    print("Bravo tu as gagné!!!")

    
jouer(Tabl)