"""

Voici un exemple de données permettant de manipuler un livre de recettes de cuisine à partir de la liste des ingrédients des recettes :
Recette
Ingrédients
Gâteau au chocolat
chocolat, œuf, farine, sucre, beurre
Gâteau au yaourt
yaourt, œuf, farine, sucre
Crêpes
œuf, farine, lait, bière
Quatre-quarts
œuf, farine, beurre, sucre
Kouign-amann
farine, beurre, sucre
On va modéliser en Python un livre de recettes, par un dictionnaire de type dict(str : list(str)) dans lequel les noms des recettes, de type str, sont les clés et l’ensemble des ingrédients, de type list(str), sont les valeurs associées.
1. Construire un dictionnaire MesRecettes correspondant au tableau ci-dessus.
2. Définir une fonction NbIngredients(D, nom) qui, à partir d’un dictionnaire de recettes D, défini comme décrit ci-dessus, renvoie le nombre d’ingrédients de la recette nommé nom.
3. Définir une fonction RechercheRecettes(D,I) renvoyant l’ensemble des recettes du dictionnaire D qui utilisent l’ingrédient I.
4. Définir une fonction RechercheRecettes2(D,I1,I2) renvoyant l’ensemble des recettes du dictionnaire D qui utilisent les ingrédients I1 et I2.
5. Définir une fonction RechercheRecettesMulti(D,LI) renvoyant l’ensemble des recettes du dictionnaire D qui utilisent tous les ingrédients de la liste LI."""

recettes = {
    "Gateau au chocolat": ["chocolat", "oeuf", "farine", "sucre", "beurre"],
    "Gateau au yaourt": ["yaourt", "oeuf", "farine", "sucre"],
    "Crepes": ["oeuf", "farine", "lait", "biere"],
    "Quatre-quarts": ["oeuf", "farine", "beurre", "sucre"],
    "Kouign-amann": ["farine", "beurre", "sucre"]
}

print(len(recettes["Gateau au chocolat"]))


def NbIngredients(D, nom):
    return len(D[nom])


def RechercheRecettes(D, I):
    return [nom for nom, ing in D.items() if I in ing]


def RechercheRecettes2(D, I1, I2):
    return [nom for nom, ing in D.items() if I1 in ing and I2 in ing]


def RechercheRecettesMulti(D, LI):
    return [nom for nom, ing in D.items() if all(i in ing for i in LI)]


print(NbIngredients(recettes, "Gateau au chocolat"))
print(RechercheRecettes(recettes, "oeuf"))
print(RechercheRecettes2(recettes, "oeuf", "sucre"))
print(RechercheRecettesMulti(recettes, ["farine", "sucre", "beurre"]))
