from time import time
import math


def rendu_monnaie_rec(pieces, s):
    """renvoie le nombre minimal de pièces pour faire la somme s avec
    le système pieces, sinon inf (pour infini, donc pas de solution)"""
    if s == 0:
        return 0
    nombre_min = math.inf
    for p in pieces:
        if p <= s:
            nombre_pieces = 1 + rendu_monnaie_rec(pieces, s - p)
            if nombre_pieces < nombre_min:
                nombre_min = nombre_pieces
    return nombre_min


def duree_rendu_monnaie_rec(pieces, s):
    """renvoie le temps d'exécution de la fonction rendu_monnaie_rec en secondes"""
    temps_debut = time()
    rendu_monnaie_rec(pieces, s)
    temps_fin = time()
    return temps_fin - temps_debut

# Tests


print(rendu_monnaie_rec([2, 5, 10], 11))
print(rendu_monnaie_rec([5, 10], 19))

for n in range(5, 50, 5):
    print(n, duree_rendu_monnaie_rec([2, 5, 10], n))
