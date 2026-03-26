import time


def fusion(lst1: list, lst2: list) -> list:
    resultat = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            resultat.append(lst1[i])
            i += 1
        else:
            resultat.append(lst2[j])
            j += 1

    # add remaining elements
    resultat += lst1[i:]
    resultat += lst2[j:]

    return resultat


def diviser(lst: list):
    mid = len(lst) // 2

    return lst[:mid], lst[mid:]


def tri_fusion(maListe: list):
    if len(maListe) <= 1:
        return maListe

    lst1, lst2 = diviser(maListe)
    lst1 = tri_fusion(lst1)
    lst2 = tri_fusion(lst2)

    return fusion(lst1, lst2)


def nombres_aleatoires(n, K):
    import random

    lst = []

    for i in range(n):
        lst.append(random.randint(0, K))

    return lst


def duree_un_tri(lst):
    start = time.perf_counter()

    tri_fusion(lst)

    end = time.perf_counter()

    return end - start


def duree_tri_fusion(n, t):
    total = 0

    for _ in range(n):
        lst = nombres_aleatoires(t, t)
        total += duree_un_tri(lst)

    return total / n


print(fusion([1, 2, 3], [2, 3, 4]))
print(diviser([1, 2, 3, 4]))
print(tri_fusion([1, 3, 4, 5, 6, 2, 7]))
print(duree_un_tri([1, 3, 4, 5, 6, 2, 7]))
print(duree_tri_fusion(10, 20))
