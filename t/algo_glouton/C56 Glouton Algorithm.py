def valeur(dico):
    return dico['valeur']

def tri_valeur(liste_objets):
    liste_objets.sort(key=valeur, reverse = True)

def masse(dico):
    return dico['masse']

def tri_masse(liste_objets):
    liste_objets.sort(key=masse, reverse=True)

def valeur_masse(dico):
    return dico['valeur']/dico['masse']

def tri_valeur_masse(liste_objets):
    liste_objets.sort(key = valeur_masse, reverse = True)

def camion_glouton(liste_objets, charge_utile, tri):
    """
    liste_objets : liste de dictionnaires, chaque dictionnaire représente un objet
    charge_utile : entier (masse maximale supportée par le camion)
    tri : Fonction de tri à choisir, correspondant aux stratégies 1, 2 ou 3

    Sortie: list : renvoie le chargement du camion obtenu par la stratégie choisie
            sous la forme d'une liste de dictionnaires (liste d'objets)
    Exemple :
    >>> objets = [{'nom' : 'A', 'valeur' : 500, 'masse' : 15}, {'nom' : 'B', 'valeur' : 400, 'masse' : 24}, {'nom' : 'C', 'valeur' : 350, 'masse' : 9}, {'nom' : 'D', 'valeur' : 750, 'masse' : 25}]
    >>> camion_glouton(objets, 40, tri_masse)
    [{'nom': 'D', 'valeur': 750, 'masse': 25}, {'nom': 'A', 'valeur': 500, 'masse': 15}]
    """
    # Tri de la liste d'objets
    tri(liste_objets)

    # Initialisation du chargement
    masse_chargee = 0
    objets_charges = []

    # Chargement
    pass


##----- programme principal -----##

objets = [{'nom' : 'A', 'valeur' : 500, 'masse' : 15}, {'nom' : 'B', 'valeur' : 400, 'masse' : 24}, {'nom' : 'C', 'valeur' : 350, 'masse' : 9}, {'nom' : 'D', 'valeur' : 750, 'masse' : 25}]

print(camion_glouton(objets, 40, tri_masse))