"""
Créez un fichier nommé POO_Exo1.py
a)   Écrivez une classe Domino pour représenter une pièce de domino. Les objets sont initialisés avec les valeurs des deux côtés, gauche et droit. Les valeurs d’un côté peut aller de blanc (= valeur 0) à 6.
b)  Ajoutez une méthode .affiche_points() qui affiche les valeurs des deux faces.
c)   Ajoutez une méthode .totale_points() qui retourne la somme de deux valeurs.
d)  Ajoutez une méthode EstDouble() qui retourne True si le côté gauche et droit ont la même valeur, et False sinon.
e)   Ajoutez une méthode ContientBlanc() si le domino possède un blanc sur l’un des côtés.
Vous devez obtenir sur la console par execution du programme :
>>> d = Domino(4, 6)
>>> d.affiche_points() face A: 4, face B: 6
>>> x = d.totale_points() >>> print(x)
10
>>> d.EstDouble() False
>>> d.ContientBlanc() False
"""


class Domino:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def affiche_points(self):
        print("face A: ", self.left)
        print("face B: ", self.right)

    def totale_points(self):
        return self.left + self.right

    def EstDouble(self):
        if self.left == self.right:
            return True
        else:
            return False

    def ContientBlanc(self):
        if self.left == 0 or self.right == 0:
            return True
        else:
            return False


d = Domino(4, 6)
d.affiche_points()
x = d.totale_points()
print(x)
print(d.EstDouble())
print(d.ContientBlanc())
