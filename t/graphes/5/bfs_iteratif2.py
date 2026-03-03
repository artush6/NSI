# Programme de l'exercice 2 de l'activité C39

from file import *


def bfs_iteratif2(G, s):
    parents = {}
    parents[s] = None
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
                    parents[voisin] = tmp

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


# A décocher pour tester la fonction bfs_iterati2

parents = bfs_iteratif2(G, 'a')
print(parents)
print(solution('h', parents))
