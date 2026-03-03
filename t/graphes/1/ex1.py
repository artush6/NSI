def nbre_amis(m, s):
    n = 0  # initialisation à 0 du nombre d'amis de l'utilisateur s
    liste_utilisateurs = ["Alice", "Bob",
                          "Chloe", "David", "Emma", "Fred", "Zoe"]
    indice = liste_utilisateurs.index(s)
    # à compléter
    for i in m[indice]:
        if i == 1:
            n += 1
    return n


### Codage de la matrice d'adjacence ###

# à compléter
m = [[0, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 0],
     [1, 0, 0, 1, 1, 1, 0],
     [1, 0, 1, 0, 0, 0, 1],
     [0, 1, 1, 0, 0, 1, 0],
     [0, 1, 1, 0, 1, 0, 0],
     [1, 0, 0, 1, 0, 0, 0]
     ]
print(m)

### Test de la fonction nbre_amis() ###

s = input("Quel est le nom de l\'utilisateur ?  ")
print(nbre_amis(m, s))
