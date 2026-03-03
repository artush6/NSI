def successeurs(s,g):
    # à compléter
    pass


def conversion1(g):
    sommets = {}
    n = 0
    for s in g:
        sommets[s] = n
        n = n + 1
    mat = [n*[0] for i in range(n)]
    # à compléter
    pass


def conversion2(m):
    sommets = {}
    n = len(m)
    for i in range(n):
        sommets[i] = i+1
    g = {}
    for i in range(n):
        g[sommets[i]] = []
    # à compléter
    pass


### Codage du dictionnaire d'adjacence ###

# à compléter
#g={}
#print(g)


### Test de la fonction successeurs() ###

#print(successeurs(1,g))
#print(successeurs(4,g))


### Test de la fonction conversion1() ###

#m=conversion1(g)
#print(m)


### Test de la fonction conversion2() ###

#print(conversion2(m))