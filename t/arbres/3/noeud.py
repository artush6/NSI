class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    """permet de tracer l'arbre, tourné de 90° sur la gauche"""
    def affichage(self, niveau=0, c=132):
        # c=132 --> code utf8 marquant la racine par un point
        if self.droit is not None:
            self.droit.affichage(niveau + 1, 47)   # code 47 --> /
        print(f"{' ' * 4 * niveau}{chr(c)}{self.valeur}")
        if self.gauche is not None:
            self.gauche.affichage(niveau + 1, 92)  # code 92 --> \


# -------------------------
# Construction de l'arbre
# -------------------------

# Racine
arbre = Noeud(10)

# Fils gauche et droit de 10
arbre.gauche = Noeud(8)
arbre.droit = Noeud(6)

# Sous-arbre gauche (noeud 8)
arbre.gauche.gauche = Noeud(7)
arbre.gauche.droit = Noeud(1)

# Sous-arbre droit (noeud 6)
arbre.droit.gauche = Noeud(11)
arbre.droit.droit = Noeud(3)

# Suite du sous-arbre gauche (noeud 7)
arbre.gauche.gauche.droit = Noeud(9)

# Sous-arbre de 11
arbre.droit.gauche.droit = Noeud(4)

# Sous-arbre de 3
arbre.droit.droit.droit = Noeud(2)

# Sous-arbre de 2
arbre.droit.droit.droit.gauche = Noeud(5)


# -------------------------
# Affichage de l'arbre
# -------------------------

arbre.affichage()
