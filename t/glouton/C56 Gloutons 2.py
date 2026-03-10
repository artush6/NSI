def masse(dico):
    """
    dico : dictionnaire qui représente un objet ayant les clés 'masse' et 'valeur'
    Sortie: integer : la masse
    Exemple :  masse({'nom': 'D', 'valeur': 750, 'masse': 25}) renvoie 25
    """
    return dico["masse"]


def tri_masse(liste_objets):
    """
    liste_objets : liste de dictionnaires, chaque dictionnaire représente un objet
    Sortie: None : Modifie en place la liste en triant les dictionnaires par ordre
            décroissant de masse (fonction à effet de bord)
    Exemple :
    >>> objets = [{'nom' : 'A', 'valeur' : 500, 'masse' : 15}, {'nom' : 'B', 'valeur' : 400, 'masse' : 24}, {'nom' : 'C', 'valeur' : 350, 'masse' : 9}, {'nom' : 'D', 'valeur' : 750, 'masse' : 25}]
    >>> tri_masse(objets)
    >>> objets
    [{'nom': 'D', 'valeur': 750, 'masse': 25}, {'nom': 'B', 'valeur': 400, 'masse': 24}, {'nom': 'A', 'valeur': 500, 'masse': 15}, {'nom': 'C', 'valeur': 350, 'masse': 9}]
    """
    return liste_objets.sort(key=masse, reverse=True)


## ----- programme principal -----##

objets = [{'nom': 'A', 'valeur': 500, 'masse': 15}, {'nom': 'B', 'valeur': 400, 'masse': 24}, {
    'nom': 'C', 'valeur': 350, 'masse': 9}, {'nom': 'D', 'valeur': 750, 'masse': 25}]
tri_masse(objets)
print(objets)
