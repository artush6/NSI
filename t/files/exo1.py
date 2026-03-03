class File:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        if len(self.contenu) != 0:
            return False
        else:
            return True

    def enfiler(self, x):
        self.contenu.append(x)

    def defiler(self):
        assert not self.est_vide, "List is full"
        self.contenu.pop(x)
