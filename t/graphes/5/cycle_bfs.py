# Programme de l'exercice 3 de l'activité C39

from file import *


def cycle_bfs(G, s):
    niveaux = {x: None for x in G}
    niveaux[s] = 0
    f = File()
    f.enfiler(s)
    while not f.est_vide():
        tmp = f.defiler()
        for voisin in G[tmp]:
            if niveaux[voisin] == None:
                niveaux[voisin] = niveaux[tmp]+1
                f.enfiler(voisin)
            elif niveaux[voisin] >= niveaux[tmp]:
                return True
    return False


G = {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'c'], 'd': ['b', 'c', 'e'], 'e': [
    'b', 'd', 'f', 'g'], 'f': ['e', 'g'], 'g': ['e', 'f', 'h'], 'h': ['g']}

G2 = {'a': ['b', 'd'], 'b': ['a', 'c', 'h'], 'c': ['b'], 'd': [
    'a', 'e', 'f', 'g'], 'e': ['d'], 'f': ['d'], 'g': ['d'], 'h': ['b']}
