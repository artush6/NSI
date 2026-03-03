"""
En 1998, deux jeunes doctorants de l’université de Stanford, Larry Page et Sergey Brin (en collaboration avec Motwani et Wynograd) publiaient un article intitulé "The PageRank Citation Ranking: Bringing Order to the Web" présentant les résultats d’un nouvel algorithme permettant de classer les pages web selon leur popularité et montrant la précision de cet algorithme sur un nouveau moteur de recherche appelé … Google  !
Voilà une version simplifiée de cet algorithme:
• On simule le comportement d’un internaute
• On démarre au hasard sur une page
• On suit de façon aléatoire un lien sur cette page
• Et ainsi de suite…
On impose le fait que dans 15 % des cas, l’utilisateur abandonne sa navigation pour repartir d’une page au hasard. Notre utilisateur va se balader de pages en pages, en faisant son petit tour du net. À chaque fois que l’utilisateur tombe sur une page donnée, cette page gagne un point. Et à la fin, la page ayant le plus de point est alors la page la plus populaire du réseau !

Considérons un cas particulier avec 6 sites web : A, B, C, D, E, F ayant des liens hypertexte entre eux.
• Le site A contient un lien vers les sites "B", "C" et "E" (3 liens sortants)
• Le site B contient un lien vers le site "F" (1 lien sortant)
• Le site C contient un lien vers les sites "A" et "E" (2 liens sortants)
• Le site D contient un lien vers les sites "B" et "C" (2 liens sortants)
• Le site E contient un lien vers les sites "A", "B", "C", "D" et "F" (5 liens sortants)
• Le site F contient un lien vers le site "E" (1 lien sortant)
1. Stocker les noms de sites dans une liste  : Websites = ["A","B","C","D","E","F"].
2. Créer un dictionnaire Hypertext dont les clés sont les sites web et les valeurs la liste des sites vers lesquels ils ont un lien sortant. Par exemple : Hypertext["A"] = ["B","C","E"].
3. Créer un dictionnaire Nombre_visites dont les clés sont les sites web et les valeurs, initialisées à 0, sont le nombre de fois où le site a été visité. Par exemple  : Nombre_visites["A"] = 0.
4. Voici l’algorithme de calcul :
from random import*
i=0
tant que i<1000
     On choisit au hasard un site qu’on affecte à la variable x
     Tant qu’un nombre aléatoire est inférieur à 0.85
          Le nombre de visite de x est incrémenté de 1
          un lien hypertexte visitable choisi de façon aléatoire est affecté à x      i=i+1
On fait afficher les résultats
• L’instruction random() renvoie un nombre dans l’intervalle [0,1[
• L’instruction x = choice(Websites) permet de choisir au hasard un site et le stocke dans x
• L’instruction x = choice(Hypertext[x]) permet de ……
Traduire cet algorithme en Python et donner le classement des sites web obtenus.
"""

from random import random, choice

# 1. Liste des sites
Websites = ["A", "B", "C", "D", "E", "F"]

# 2. Dictionnaire des liens sortants
Hypertext = {
    "A": ["B", "C", "E"],
    "B": ["F"],
    "C": ["A", "E"],
    "D": ["B", "C"],
    "E": ["A", "B", "C", "D", "F"],
    "F": ["E"]
}

# 3. Dictionnaire du nombre de visites
Nombre_visites = {site: 0 for site in Websites}

# 4. Simulation
i = 0
while i < 1000:
    # choix d’un site de départ
    x = choice(Websites)
    # navigation
    while random() < 0.85:  # probabilité de continuer
        Nombre_visites[x] += 1
        x = choice(Hypertext[x])  # suivre un lien
    i += 1

# Affichage du classement
classement = sorted(Nombre_visites.items(), key=lambda kv: kv[1], reverse=True)
print("Résultats :")
for site, score in classement:
    print(site, ":", score)
