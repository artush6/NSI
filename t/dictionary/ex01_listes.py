"""

Voici un dictionnaire de tuples : mes_points={"A":(1,3),"B":(– 5,6),"C":(2,– 8)}
Les clés sont les noms des points, de type str et les valeurs associées sont les coordonnées de ces points dans un repère plan, de type tuple.
1. Construire, en Python, un dictionnaire  mes_points correspondant aux valeurs ci-dessus.
2. Coder la commande qui permet de rajouter en entrée le point D(– 2,5).
3. Coder la commande qui permet d’afficher l’abscisse de B.
4. Coder la commande qui permet d’afficher l’ordonnée de D.
5. Coder le calcul qui permet d’obtenir la distance AC.

"""


def points(mes_points: dict = {"A": (1, 3), "B": (-5, 6), "C": (2, -8)}) -> dict:
    mes_points["D"] = (-2, 5)
    print(mes_points)
    print(mes_points["B"][0])
    print(mes_points["D"][1])
    print(((mes_points["A"][0] - mes_points["C"][0]) ** 2 +
          (mes_points["A"][1] - mes_points["C"][1]) ** 2) ** 0.5)


points()
