class File:
    """Classe File"""

    def __init__(self):
        """Initialisation d'une file vide de type liste Python"""
        self.contenu = []

    def est_vide(self):
        """Test si la file est vide (retourne True) ou non (retourne False)"""
        return self.contenu == []

    def enfiler(self, x):
        """Enfile un élément x au sommet de la file qui est à droite"""
        self.contenu.append(x)

    def defiler(self):
        """Defile le sommet de la file et le retourne"""
        assert not self.est_vide(), "File vide !"
        return self.contenu.pop(0)  # ou del self.file[-1]

    def taille(self):
        return len(self.contenu)

    def sommet(self):
        assert not self.est_vide(), "File vide !"
        return self.contenu[0]

    def present(self, x):
        """Test si x est dans la file"""
        return x in self.contenu
