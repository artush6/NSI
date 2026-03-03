class Arbre:
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
              
    def get_valeur(self):
      return self.valeur
    def get_gauche(self):
      return self.gauche

    def get_droite(self):
      return self.droit
    
    def insertion_gauche(self, val):
      assert self.gauche is None, "Sous-arbre gauche non vide !"
      self.gauche = Arbre(val)
      
    def insertion_droite(self, val):
      assert self.gauche is None, "Sous-arbre droit non vide !"
      self.droit = Arbre(val)

      


# -------------------------
# Construction de l'arbre
# -------------------------

# Racine
arbre = Arbre(10)

# Fils gauche et droit de 10
arbre.gauche = Arbre(8)
arbre.droit = Arbre(6)

# Sous-arbre gauche (Arbre 8)
arbre.gauche.gauche = Arbre(7)
arbre.gauche.droit = Arbre(1)

# Sous-arbre droit (Arbre 6)
arbre.droit.gauche = Arbre(11)
arbre.droit.droit = Arbre(3)

# Suite du sous-arbre gauche (Arbre 7)
arbre.gauche.gauche.droit = Arbre(9)

# Sous-arbre de 11
arbre.droit.gauche.droit = Arbre(4)

# Sous-arbre de 3
arbre.droit.droit.droit = Arbre(2)

# Sous-arbre de 2
arbre.droit.droit.droit.gauche = Arbre(5)


# -------------------------
# Affichage de l'arbre
# -------------------------

arbre.affichage()
