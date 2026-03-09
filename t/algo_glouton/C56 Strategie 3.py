def valeur_masse(dico):
    """
    dico : dictionnaire qui représente un objet ayant les clés 'masse' et 'valeur'
    Sortie: float : le rapport valeur/masse
    Exemple : valeur_masse({'nom': 'D', 'valeur': 750, 'masse': 25}) renvoie 30.0
    """
    pass


def tri_valeur_masse(liste_objets):
    """
    liste_objets : liste de dictionnaires, chaque dictionnaire représente un objet
    Sortie: None : Modifie en place la liste en triant les dictionnaires par ordre
            décroissant de rapport valeur/masse (fonction à effet de bord)
    Exemple :
    >>> objets = [{'nom' : 'A', 'valeur' : 500, 'masse' : 15}, {'nom' : 'B', 'valeur' : 400, 'masse' : 24}, {'nom' : 'C', 'valeur' : 350, 'masse' : 9}, {'nom' : 'D', 'valeur' : 750, 'masse' : 25}]
    >>> tri_valeur_masse(objets)
    >>> objets
    [{'nom': 'C', 'valeur': 350, 'masse': 9}, {'nom': 'A', 'valeur': 500, 'masse': 15}, {'nom': 'D', 'valeur': 750, 'masse': 25}, {'nom': 'B', 'valeur': 400, 'masse': 24}]
    """
    pass


##----- programme principal -----##

objets = [{'nom' : 'A', 'valeur' : 500, 'masse' : 15}, {'nom' : 'B', 'valeur' : 400, 'masse' : 24}, {'nom' : 'C', 'valeur' : 350, 'masse' : 9}, {'nom' : 'D', 'valeur' : 750, 'masse' : 25}]
tri_valeur_masse(objets)
print(objets)
