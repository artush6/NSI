from operator import truediv
import pygame
from pygame.locals import *
from random import randint, choice
from sys import exit
import matplotlib.pyplot as plt
from pile import Pile


class Case:
    def __init__(self):
        # à compléter : exercice n°1
        self.murN = True
        self.murW = True
        self.murS = True
        self.murE = True
        self.vue = False

    def __repr__(self):
        return f"C(N={int(self.murN)},S={int(self.murS)},E={int(self.murE)},W={int(self.murW)},V={int(self.vue)})"


class Labyrinthe:
    def __init__(self, largeur, hauteur):
        # à compléter : exercice n°2
        self.largeur = largeur
        self.hauteur = hauteur

        # grille de cases
        self.laby = [[Case() for j in range(hauteur)] for i in range(largeur)]

    def __directions_possibles(self, i, j):
        # code à décommenter et à compléter : exercice n°4

        directions = []

        # Sud
        if j < self.hauteur-1 and not self.laby[i][j+1].vue:
            directions.append('S')

        # Nord
        if j > 0 and not self.laby[i][j-1].vue:
            directions.append('N')

        # Est
        if i < self.largeur - 1 and not self.laby[i+1][j].vue:
            directions.append('E')

        # Ouest
        if i > 0 and not self.laby[i-1][j].vue:
            directions.append('W')

        return directions

    def __abattre_mur(self, i, j, dir, pile):
        # code à décommenter et à compléter : exercice n°5

        if dir == 'S':  # on se dirige vers le sud
            # on abat le mur sud de la case courante
            self.laby[i][j].murS = False
            # on abat le mur nord de la case située en-dessous de la case courante
            self.laby[i][j+1].murN = False
            # cette case est alors marquée comme vue
            self.laby[i][j+1].vue = True
            # on stocke les coordonnées de cette case dans la pile
            pile.empiler((i, j+1))
        elif dir == 'N':
            self.laby[i][j].murN = False
            self.laby[i][j-1].murS = False
            self.laby[i][j-1].vue = True
            pile.empiler((i, j-1))

        elif dir == 'E':
            self.laby[i][j].murE = False
            self.laby[i+1][j].murW = False
            self.laby[i+1][j].vue = True
            pile.empiler((i+1, j))

        elif dir == 'W':
            self.laby[i][j].murW = False
            self.laby[i-1][j].murE = False
            self.laby[i-1][j].vue = True
            pile.empiler((i-1, j))
        pass

    def generer(self):
        pile = Pile()

        # choisir une case de départ aléatoire
        i = randint(0, self.largeur - 1)
        j = randint(0, self.hauteur - 1)

        # marquer comme vue et empiler
        self.laby[i][j].vue = True
        pile.empiler((i, j))

        while not pile.est_vide():
            i, j = pile.depiler()

            directions = self.__directions_possibles(i, j)

            if len(directions) > 0:
                pile.empiler((i, j))
                dir = choice(directions)

                self.__abattre_mur(i, j, dir, pile)

    def afficher(self):
        for i in range(self.largeur):
            color = "g"
            for j in range(self.hauteur):
                if self.laby[i][j].murS:
                    plt.plot([i, i+1], [j+1, j+1], color)
                if self.laby[i][j].murW:
                    plt.plot([i, i], [j, j+1], color)
        plt.gca().invert_yaxis()
        # contour nord du labyrinthe
        plt.plot([0, self.largeur], [0, 0], color)
        plt.plot([self.largeur, self.largeur], [0, self.hauteur],
                 color)  # contour est du labyrinthe
        plt.show()


laby = Labyrinthe(20, 20)
print(laby.laby)
laby.generer()
laby.afficher()
