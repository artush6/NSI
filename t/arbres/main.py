def creer_arbre(r=None):
    """renvoie un arbre vide ou un arbre dont la racine a la valeur r"""
    if r == None:
        return []
    else:
        return [r, [], []]
