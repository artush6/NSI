"""def recherche_naive(texte: str, motif: str):
    lst = [i for i in texte]
    mot = [j for j in motif]

    resultats = []

    n = len(lst)
    m = len(mot)

    for i in range(n - m + 1):
        j = 0
        trouve = True

        while j < m and trouve:
            if lst[i + j] == mot[j]:
                j += 1
            else:
                trouve = False

        if trouve:
            resultats.append(i)

    return resultats"""


def recherche_naive(texte, motif):
    resultats = []

    n = len(texte)
    m = len(motif)

    for i in range(n - m + 1):
        trouve = True

        for j in range(m):
            if texte[i + j] != motif[j]:
                trouve = False

        if trouve:
            resultats.append(i)

    return resultats


print(recherche_naive("aacabacabaabaa", "abaa"))


print(recherche_naive('aacabacabaabaa', 'abaa'))
