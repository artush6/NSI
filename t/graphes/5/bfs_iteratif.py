# Programme de l'exercice 1 de l'activité C39

from file import *


def bfs_iteratif(G, s):
    sommets_visites = []
    f = File()
    f.enfiler(s)
    while not f.est_vide():
        tmp = f.defiler()
        if tmp not in sommets_visites:
            sommets_visites.append(tmp)

            for voisin in G[tmp]:
                if voisin not in sommets_visites and not f.present(voisin):
                    f.enfiler(voisin)

    return sommets_visites


G = {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'c'], 'd': ['b', 'c', 'e'], 'e': [
    'b', 'd', 'f', 'g'], 'f': ['e', 'g'], 'g': ['e', 'f', 'h'], 'h': ['g']}
print(bfs_iteratif(G, 'g'))
