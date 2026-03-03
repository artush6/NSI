def nbre_amis(m, s):
    n1 = 0  # initialisation à 0 du nombre d'amis que s suit
    n2 = 0  # initialisation à 0 du nombre de personnes qui suivent s
    liste_utilisateurs = ["Alice", "Bob",
                          "Chloe", "David", "Emma", "Fred", "Zoe"]
    indice = liste_utilisateurs.index(s)
    # à compléter
    for i in m[indice]:
        if i == 1:
            n1 += 1
    for j in m:
        if j[indice] == 1:
            n2 += 1
    return n1, n2


### Codage de la matrice d'adjacence ###
# à compléter
m = [[0, 0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 1],
     [1, 0, 0, 1, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0]]
print(m)

### Test de la fonction nbre_amis() ###

utilisateurs = ["Alice", "Bob", "Chloe", "David", "Emma", "Fred", "Zoe"]
for s in utilisateurs:
    print(s, "->", nbre_amis(m, s))
