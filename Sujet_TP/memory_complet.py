import numpy as np
import random

"""
@author vcoindet
Jeu de memory
"""

#Tabl = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f']

def melange_carte(Tab):
    """
        Mélange aléatoirement une liste
        :param Tab: liste représentant les cartes
        :param type: list
        :return: liste de cartes mélangées
        :rtype: list
    """
    for i in range(1, len(Tab)):
        # pick an element in Tab[:i+1] with which to exchange Tab[i]
        j = int(random.random() * (i+1))
        Tab[i], Tab[j] = Tab[j], Tab[i]
    return Tab

def carte_cache(Tab):
    """
        Crée une liste de 0 de même longeur que Tab
        :param Tab: liste qui représente les cartes à faire deviner
        :param type: list
        :return: liste de 0
        :rtype: list
    """
    Tab_cache = []
    for i in range(len(Tab)):
        Tab_cache.append(0)
    return Tab_cache


def choisir_cartes(Tab):
    """
        Crée une liste de 0 de même longeur que Tab
        :param Tab: liste qui représente les cartes à faire deviner
        :param type: list
        :return: liste de 0
        :rtype: list
    """
    c1 = int(input("Choisissez l'index d'une carte : "))
    if(c1 > len(Tab) - 1):
        c1 = int(input('Nope, choisissez un autre index entre 0 et ' + str(len(Tab)) + ' : '))
    print(Tab[c1])
    c2 = int(input("Choisissez l'index d'une deuxieme carte : "))
    if(c2 > len(Tab) - 1):
        c2 = int(input('Nope, choisissez un autre index entre 0 et ' + str(len(Tab)) + ' : '))
    while c1 == c2:
        print("Erreur, la deuxieme carte ne peut être la même que la premiere ! ")
        c2 = int(input("Veuillez choisir une deuxieme carte différente de la premiere : "))
        if(c2 > len(Tab) - 1):
            c2 = int(input('Nope, choisissez un autre index entre 0 et ' + str(len(Tab)) + ' : '))
    print(Tab[c2])
    return [c1,c2]


def retourne_carte (c1, c2, Tab, Tab_cache):
    """
        Remplace les 0 par les vraies lettres/cartes
        :param c1: index carte 1
        :param type: Integer
        :param c2: index carte 2
        :param type: Integer
        :param Tab: liste de carte à trouver
        :param type: List
        :param Tab_cache: liste de 0
        :param type: List
        :return: liste de 0 mis à jour (des 0 ont été remplacés par des lettres)
        :rtype: List
    """
    if Tab[c1] == Tab[c2]:
        Tab_cache[c1] = Tab[c1]               
        Tab_cache[c2] = Tab[c2]
        
    return Tab_cache

def jouer(Tab):
    """
        Fonction qui permet de lancer le jeu jusqu'à ce que fin s'en suive
        :param Tab: la liste des cartes
        :param type: List
    """
    print("Bienvenue sur notre Jeu Memory, ci dessous voici les cartes mise en jeu. Il y en a 12")
    print(Tab)
    Tab = melange_carte(Tab)
    print("Maintenant nous allonss melanger les cartes et les retourner")
    
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

# Tests
if __name__ == "__main__":   
    #Test melange_carte
    print("Test melange_carte :")
    Tabl = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f']
    print(melange_carte(Tabl))
    
    #Test carte_cache(Tab):
    print("Test carte_cache :")
    tab_c =carte_cache(Tabl)
    print(tab_c)
    
    #Test choisir_cartes(Tab):
    print("Test choisir_carte :")
    #choisir_cartes(Tabl)
    
    #Test retourne_carte (c1, c2, Tab, Tab_cache):
    print("Test retourne_carte :")
    Tabl2 = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f']
    print(retourne_carte(0, 1, Tabl2, tab_c))
    jouer(Tabl)