
##########################################################
##                    Séance C32_Arbre4                 ##
##               Fichier Arbre-parcours.py              ##
##                       VERSION ELEVE                  ##      ##########################################################

import pilefile as pf


class Arbre:
    def __init__(self, info=None, fg=None, fd=None):
        self.info = info  # étiquette du noeud
        self.fg = fg      # fils gauche = sous-arbre gauche
        self.fd = fd      # fils droite = sous-arbre droit

    def estVide(self):
        return self.info == None

    def insererElement(self, e):
        if self.estVide():   # le sous arbre est vide
            self.info = e
        else:
            if e < self.info:
                if self.fg:  # le sous arbre existe deja, on continue
                    self.fg.insererElement(e)
                else:  # le sous arbre n'existe pas, on le créer
                    self.fg = Arbre(e)
            ######
            #A compléter au niveau de l'exercice 2
            elif e > self.info: 
                if self.fd: 
                    self.fd.insererElement(e)
                else: 
                    self.fd = Arbre(e)
            ######
            # rien à faire si égal, déjà présent, arrêt de la récursion
            else: 
                return


    def hauteurArbre(self):
        if self.estVide(): return -1
        hgauche = self.fg.hauteurArbre() if self.fg else -1
        hdroit = self.fd.hauteurArbre() if self.fd else -1
        if hgauche > hdroit:
            return hgauche + 1
        else:
            return hdroit + 1

    def afficherArbre(self):  # il n'est pas utile d'étudier cette méthode, elle sert à afficher l'arbre
        if self.estVide(): return
        print()
        h = self.hauteurArbre()
        f = pf.File([])
        ind_racine = ((2 ** h) * 2 - 2) // 2
        decalage = (2 ** h)
        f.enfiler((self, ind_racine, decalage))
        liste = []
        liste.append((self, ind_racine, decalage))
        while not f.estVide():
            (n, i, d) = f.traiter()
            if n.fg:
                f.enfiler((n.fg, i - d // 2, d // 2))
                liste.append((n.fg, i - d // 2, d // 2))
            if n.fd:
                f.enfiler((n.fd, i + d // 2, d // 2))
                liste.append((n.fd, i + d // 2, d // 2))
        (n, i, d) = liste[0]
        for _ in range(d - 2):
            print(' ', end='')
        print(str(n.info), end='')
        (nprec, iprec, dprec) = (n, i, d)
        for (n, i, d) in liste[1:]:
            if d != dprec:
                print()
                iprec = -1
            for _ in range(i - iprec - 1):
                print(' ', end='')
            print(str(n.info), end='')
            (nprec, iprec, dprec) = (n, i, d)
        print()
        print()


## Méthodes de parcours en profondeur   
    # A faire au niveau de l'exercice 3

    def afficherParcoursPrefixe(self):
        if self.estVide():
            return
        print(self.info, end=' ') # on traite le noeud
        if self.fg:
            self.fg.afficherParcoursPrefixe()
        if self.fd: 
            self.fd.afficherParcoursPrefixe()

    def afficherParcoursInfixe(self):
        if self.estVide():
            return
        if self.fg :
            self.fg.afficherParcoursInfixe()
        print(self.info, end=' ') # on traite le noeud 
        if self.fd :
            self.fd.afficherParcoursInfixe()

    def afficherParcoursSuffixe(self):
        if self.estVide():
            return
        if self.fg:
            self.fg.afficherParcoursSuffixe()   # d'abord le fils gauche
        if self.fd:
            self.fd.afficherParcoursSuffixe()   # puis le fils droit
        print(self.info, end=' ')               # puis le noeud


    def afficherParcoursIteratif(self):
        if self.estVide(): 
            return
        p = pf.Pile([])
        p.empiler(self)
        while not p.estVide():
            n = p.sommet()
            p.depiler()
            print(n.info, end = '')
            if n.fd: 
                p.empiler(n.fd)
            if n.fg: 
                p.empiler(n.fg)

    ## Méthodes de parcours en largeur
    # A faire au niveau de l'exercice 4

    def afficherParcoursLargeur(self):
        if self.estVide():
            return
        f = pf.File([])
        f.enfiler(self)
        while not f.estVide():
            n = f.traiter()
            print(n.info, end = '')
            if n.fg: 
                f.enfiler(n.fg)
            if n.fd: 
                f.enfiler(n.fd)

    ## Méthodes de recherche d'un élément d'un ABR
    # A faire au niveau de l'exercice 5

    def rechercherElement(self, e):
        if self.estVide():
            return False
        
        if e == self.info: 
            return True
        
        if e < self.info: 
            if self.fg: 
                return self.fg.rechercherElement(e)
            else:
                return False
        
        if e > self.info: 
            if self.fd: 
                return self.fd.rechercherElement(e)
            else: 
                return False

    def rechercherElementIteratif(self, e):
        pass



# ========================== programme principal =====================================

## Exercice2 : Construire l'arbre


arbre = Arbre()

print("Ajout des elements 5 2 4 1 6 9 8 10 7 3 : ")
print()
print()
arbre.insererElement(5)
arbre.insererElement(2)
arbre.insererElement(4)
arbre.insererElement(1)
arbre.insererElement(6)
arbre.insererElement(9)
arbre.insererElement(8)
arbre.insererElement(10)
arbre.insererElement(7)
arbre.insererElement(3)
arbre.afficherArbre()
print()
print()



## Exercice3 : Parcours en profondeur


print("Arbre non binaire de l'exemple avec les éléments  1 2 3 4 5 6 : ")
print()
print()
arbre2 = Arbre(1,Arbre(2),Arbre(3))
arbre2.fg.fg=Arbre(4)
arbre2.fg.fd=Arbre(5)
arbre2.fd.fd=Arbre(6)
arbre2.afficherArbre()
print()
print()
print("Le parcours en ordre préfixe :",end= ' ')
arbre2.afficherParcoursPrefixe()
print()
print("Le parcours en ordre infixe :",end= ' ')
arbre2.afficherParcoursInfixe()
print()
print("Le parcours en ordre suffixe :",end= ' ')
arbre2.afficherParcoursSuffixe()
print()


## Exercice4 : Parcours en largeur

"""
print("Arbre non binaire avec les éléments  1 2 3 4 5 6 : ")
print()
print()
arbre3 = Arbre(1,Arbre(2),Arbre(3))
arbre3.fg.fg=Arbre(4)
arbre3.fg.fd=Arbre(5)
arbre3.fd.fd=Arbre(6)
arbre3.afficherArbre()
print()
print()
print("Le parcours en largeur :",end= ' ')
arbre3.afficherParcoursLargeur()
print()
"""

## Exercice5 : Recherche d'un élément

