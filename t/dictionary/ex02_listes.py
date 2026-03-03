"""
Concevoir un dictionnaire mes_films avec 2 ou 3 exemples, qui contient des titres de films et différentes informations sur ces films : leur genre, le.s réalisatrice·s ou réalisateur·s, leur durée et l’année de sortie… Le titre est la clé et les informations, de type list, sont les valeurs associées.
Puis écrire quelques commandes qui permettent d’accéder à quelques valeurs en particulier.
On pourra imaginer une fonction qui prend en paramètres un titre de film, le dictionnaire mes_films et qui affiche les informations si le film est répertorié…
"""

mes_films = {
    "Inception": ["Science-fiction", "Christopher Nolan", 148, 2010],
    "Parasite": ["Thriller", "Bong Joon-ho", 132, 2019],
    "Amélie Poulain": ["Comédie romantique", "Jean-Pierre Jeunet", 122, 2001]
}


def infos_film(titre, dico):
    if titre in dico:
        infos = dico[titre]
        print(f"Titre : {titre}")
        print(f"Genre : {infos[0]}")
        print(f"Réalisateur : {infos[1]}")
        print(f"Durée : {infos[2]} minutes")
        print(f"Année de sortie : {infos[3]}")
    else:
        print(f"Le film '{titre}' n'est pas répertorié.")


infos_film("Parasite", mes_films)
infos_film("Avatar", mes_films)
