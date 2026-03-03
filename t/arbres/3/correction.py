# Programme de la séance C31 sur les arbres en Terminale NSI

class Arbre:
    """un noeud d'un arbre binaire"""

    def __init__(self, v, fg=None, fd=None):
        self.valeur = v      # valeur du noeud
        self.gauche = fg     # sous-arbre gauche
        self.droit = fd      # sous-arbre droit

    """permet de tracer l'arbre, tourné de 90° sur la gauche"""
    def affichage(self, niveau=0, c=132):
        # c=132 --> code utf8 marquant la racine par un point
        if self.droit is not None:
            self.droit.affichage(niveau + 1, 47)   # /
        print(f"{' ' * 4 * niveau}{chr(c)}{self.valeur}")
        if self.gauche is not None:
            self.gauche.affichage(niveau + 1, 92)  # \

    def insertion_gauche(self, valeur):
        assert self.gauche is None, "Sous-arbre gauche non vide !"
        self.gauche = Arbre(valeur)

    def insertion_droite(self, valeur):
        assert self.droit is None, "Sous-arbre droite non vide !"
        self.droit = Arbre(valeur)

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.gauche

    def get_droite(self):
        return self.droit


def taille(tree):
    if tree is None:
        return 0
    return 1 + taille(tree.gauche) + taille(tree.droit)


def hauteur(tree):
    if tree is None:
        return 0
    return 1 + max(hauteur(tree.gauche), hauteur(tree.droit))


# Construction de l'arbre (selon l'exemple du cours)
arbre = Arbre(10)

arbre.insertion_gauche(8)
arbre.insertion_droite(6)

noeud8 = arbre.get_gauche()
noeud8.insertion_gauche(7)
noeud8.insertion_droite(1)

noeud6 = arbre.get_droite()
noeud6.insertion_gauche(11)
noeud6.insertion_droite(3)

noeud7 = noeud8.get_gauche()
noeud7.insertion_droite(9)

noeud11 = noeud6.get_gauche()
noeud11.insertion_droite(4)

noeud3 = noeud6.get_droite()
noeud3.insertion_droite(2)

noeud2 = noeud3.get_droite()
noeud2.insertion_gauche(5)

print("Taille =", taille(arbre))
print("Hauteur =", hauteur(arbre))
arbre.affichage()
