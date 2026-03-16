from time import time
import math

def rendu_monnaie_rec(pieces,s):
    """renvoie le nombre minimal de pièces pour faire la somme s avec
    le système pieces, sinon inf (pour infini, donc pas de solution)"""
    if s==0:
        return ???  # à compléter
    nombre_min=math.inf # initialisation du minimum à une valeur inatteignable, l'infini !!
    for p in pieces:
        if ??? : # à compléter
            nombre_pieces= ???  # à compléter
            if nombre_pieces<nombre_min:
                ??? # à compléter
    return ???   # à compléter

def duree_rendu_monnaie_rec(pieces,s):
    """renvoie le temps d'exécution de la fonction rendu_monnaie_rec en secondes"""
    temps_debut=time()
    rendu_monnaie_rec(pieces,s)
    temps_fin=time()
    return temps_fin-temps_debut


### à décocher et à compléter pour tester """

"""print(rendu_monnaie_rec([2,5,10],11))
print(rendu_monnaie_rec([5,10],19))
for n in range(    ):    # à compléter
    print(n,duree_rendu_monnaie_rec([2,5,10],n))"""
