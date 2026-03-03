"""
Créez un fichier nommé POO_Exo2.py dans le même répertoire que le fichier de l’exercice précédent.
a)   Afin de pouvoir utiliser la classe Domino de l’exercice précédent, commencez votre programme par : from POO_Exo1 import Domino
b)   Créez une classe JeuDomino contenant dans son constructeur un attribut nommé self.Lejeu. Cet attribut est initialisé avec une liste vide. 
c) Toujours dans le constructeur de cette classe, remplissez la liste de l’attribut self.Lejeu avec les 28 dominos différents : le premier étant Domino(0,0)  et le dernier Domino(6,6). Attention, le Domino(1,0) et le Domino(0,1) sont identiques, il ne doit apparaitre qu’une seule fois.
d)  Toujours dans le constructeur __init__ ajouter l’attribut nombre auquel on affecte le nombre de dominos du jeu.
e)   Ajoutez une méthode .AfficheJeu() qui affiche le nombre de points de chaque domino, l’un en dessous de l’autre. Vérifiez à cette occasion que vous avez bien seulement 28 dominos.
f)   Ajoutez une méthode .MelangeJeu() qui mélangera l’ordre des éléments de l’attribut LeJeu. Vous pouvez utiliser pour cela la méthode shuffle de la librairie random.
g)   Ajoutez une méthode .MelangeCote() qui mélangera de façon équiprobable la valeur gauche et la valeur droite de chaque domino.



a)   Créez une méthode pour distribuer le jeu selon deux joueurs (7 dominos par personne) avec une pioche 
ordonnée (on pioche toujours en haut de la pile).
b)  Créez la possibilité de jouer à un contre un (en mode ouvert, donc on voit les dominos de l’adversaire) 
avec gestion de l’affichage. 


"""
from exo1 import Domino
import random


class JeuDomino:
    def __init__(self):
        self.Lejeu = []

        # Remplissage des 28 dominos différents
        for i in range(7):        # valeurs de 0 à 6
            for j in range(i, 7):  # évite doublons (0,1) et (1,0)
                self.Lejeu.append(Domino(i, j))

        # Attribut nombre = taille du jeu
        self.nombre = len(self.Lejeu)

    def AfficheJeu(self):
        print(f"Le jeu contient {self.nombre} dominos :")
        for d in self.Lejeu:
            d.affiche_points()

    def MelangeJeu(self):
        random.shuffle(self.Lejeu)

    def MelangeCote(self):
        for d in self.Lejeu:
            if random.choice([True, False]):  # 50% de chance
                d.left, d.right = d.right, d.left

    # --- a) Distribution à 2 joueurs ---
    def Distribuer(self):
        """Retourne deux mains de 7 dominos + une pioche."""
        self.MelangeJeu()  # mélange du jeu avant distribution
        joueur1 = self.Lejeu[:7]
        joueur2 = self.Lejeu[7:14]
        pioche = self.Lejeu[14:]
        return joueur1, joueur2, pioche

    # --- b) Mode de jeu simple ---
    def Jouer1v1(self):
        """Mode ouvert : affiche les mains des 2 joueurs et la pioche."""
        j1, j2, pioche = self.Distribuer()

        print("\n=== Distribution ===")
        print("\nMain du Joueur 1 :")
        for d in j1:
            d.affiche_points()

        print("\nMain du Joueur 2 :")
        for d in j2:
            d.affiche_points()

        print(f"\nPioche ({len(pioche)} dominos restants) :")
        for d in pioche:
            d.affiche_points()


# Exemple d’utilisation
if __name__ == "__main__":
    jeu = JeuDomino()
    jeu.AfficheJeu()

    print("\n--- Mélange du jeu ---")
    jeu.MelangeJeu()
    jeu.AfficheJeu()

    print("\n--- Mélange des côtés ---")
    jeu.MelangeCote()
    jeu.AfficheJeu()

    print("\n--- Distribution et partie 1v1 ---")
    jeu.Jouer1v1()
