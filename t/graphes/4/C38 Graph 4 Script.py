# Programme de l'exercice 3 de l'activité C38
from Pile import *
import random


def dfs_iteratif(G, s):
    sommets_visites = []
    p = Pile()
    sommets_visites.append(s)
    p.empiler(s)

    while not p.est_vide():
        tmp = s
        voisins = [v for v in G[tmp] if v not in sommets_visites]

        if voisins:
            v = random.choice(voisins)
            sommets_visites.append(v)
            p.empiler(v)
        else:
            p.depiler()
    return sommets_visites


def dfs_recursif2(G, s, parents, visite=[]):
    if s not in visite:
        visite.append(s)
        voisins = [v for v in G[s] if v not in visite]
        for v in voisins:
            parents[v] = s
            dfs_recursif2(G, v, parents, visite)
    return parents


def solution(arrivee, parents):
    chemin = []
    courant = arrivee
    while courant != None:
        chemin = [courant]+chemin
        courant = parents[courant]
    return chemin


G = {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'c'], 'd': ['b', 'c', 'e'], 'e': [
    'b', 'd', 'f', 'g'], 'f': ['e', 'g'], 'g': ['e', 'f', 'h'], 'h': ['g']}

# A décocher pour tester la fonction dfs_recursif2

parents = {'a': None}
parents = dfs_recursif2(G, 'a', parents)
print(parents)
print(solution('h', parents))
