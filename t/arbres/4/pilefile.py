
##########################################################
##                    Séance C32_Arbre4                 ##
## Fichier nécessaire pour le fichier Arbre-parcours.py ##
##########################################################

# ======================    Pile    ==============================================
class Pile :
    def __init__(self, L):
        self.liste = L

    def __repr__(self):  # ou __str__
        s = 'pile: '
        for e in self.liste:
            s += str(e) + ' '
        return s

    def empiler(self, e):
        ##
        # A compléter et retirer le mot pass
        self.liste.insert(0, e)
        ##

    def depiler(self):
        del self.liste[0]

    def sommet(self):
        return self.liste[0]

    def estVide(self):
        return len(self.liste) == 0

    def hauteur(self):
        return len(self.liste)

    def traiter(self):
        e = self.liste[0]
        del self.liste[0]
        return e

# ======================    File    ==============================================
class File :
    def __init__(self, L):
        self.liste = L

    def __repr__(self):  # ou __str__
        s = 'file: '
        for e in self.liste:
            s += str(e) + ' '
        return s

    def traiter(self):
        ##
        # A compléter et retirer le mot pass
        e = self.liste[-1]
        del self.liste[-1]
        return e
        ##

    def enfiler(self, e):
        self.liste.insert(0, e)

    def estVide(self):
        return len(self.liste) == 0

    def longueur(self):
        return len(self.liste)


# ========================== programme principal =====================================

# === Tests Pile ===
'''
L = [0]
pile = Pile(L)
print("Ajout de 5 2 4 : ", end='')
pile.empiler(5)
pile.empiler(2)
pile.empiler(4)
print(pile)

print("Suppression du sommet : ", end='')
pile.depiler()
print(pile)

print("Valeur du sommet : ", end='')
print(pile.sommet())

print("Hauteur de la pile: ", end='')
print(pile.hauteur())

print("Traiter pile : ", end='')
print("Element supprime : " + str(pile.traiter()))
print("Nouvelle pile : ", end='')
print(pile)
'''

# === Tests File ===
'''
L = [0]
file = File(L)
print("Ajout en queue de 5 2 4 : ", end='')
file.enfiler(5)
file.enfiler(2)
file.enfiler(4)
print(file)

print("Traiter file : ", end='')
print("Element supprime : " + str(file.traiter()))
print("Nouvelle file : ", end='')
print(file)

print("Longueur de la file: ", end='')
print(file.longueur())
'''