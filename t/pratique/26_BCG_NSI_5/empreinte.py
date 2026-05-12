import json

########### Fonctions données ###########


def chargement_json(nom_fichier):
    """Charge le contenu d'un fichier JSON dans un dictionnaire Python renvoyé"""
    with open(nom_fichier, "r", encoding="utf8") as curseur:
        return json.load(curseur)


def est_dictionnaire(objet):
    """Teste si un objet est de type dictionnaire"""
    return isinstance(objet, dict)


##########################################


# Première fonction à implémenter après avoir découvert le fichier JSON agrégé
# Cf fichier `empreinte_ada_agr.json`
def total_simple(empreinte):
    """Fonction qui renvoie l'empreinte carbone totale d'un dictionnaire associant
    une empreinte carbone à des noms de catégories"""
    pass


# Deuxième fonction : il faut la récursivité pour le cas des sous-catégories
# Cf fichier `empreinte_ada.json`
def total_rec(empreinte):
    """Fonction récursive qui renvoie l'empreinte carbone totale représentée
    par un dictionnaire dont les valeurs peuvent aussi être des dictionnaires"""
    pass


def test_total_rec():
    test_dico1 = {"a": 1, "d": 2}
    assert total_rec(test_dico1) == 3
    test_dico2 = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
    assert total_rec(test_dico2) == 6

# ==========================================
# Fonction à analyser et corriger (Question 3)
# ==========================================


def alerte_valeur_aberrante(empreinte, limite):
    """
    Fonction censée déterminer si au moins une valeur du dictionnaire
    dépasse strictement la limite donnée.
    """
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            return alerte_valeur_aberrante(valeur, limite)
        else:
            if valeur > limite:
                return True
    return False


# --------------------------------------------------------


def chargement_json(nom_fichier):
    with open(nom_fichier, "r", encoding="utf8") as curseur:
        return json.load(curseur)


def est_dictionnaire(objet):
    return isinstance(objet, dict)


def total_simple(empreinte):
    total = 0
    for categorie, valeur in empreinte.items():
        total += valeur
    return total


def total_rec(empreinte):
    total = 0
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            total += total_rec(valeur)
        else:
            total += valeur
    return total


def test_total_rec():
    test_dico1 = {"a": 1, "d": 2}
    assert total_rec(test_dico1) == 3

    test_dico2 = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
    assert total_rec(test_dico2) == 6

    test_dico3 = {
        "a": {
            "b": {
                "c": 10
            }
        },
        "d": 5
    }
    assert total_rec(test_dico3) == 15


def alerte_valeur_aberrante(empreinte, limite):
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            if alerte_valeur_aberrante(valeur, limite):
                return True
        else:
            if valeur > limite:
                return True
    return False


empreinte_agr = chargement_json("empreinte_ada_agr.json")
print(total_simple(empreinte_agr))

empreinte = chargement_json("empreinte_ada.json")
print(total_rec(empreinte))

test_total_rec()

print(alerte_valeur_aberrante(empreinte, 1000))
