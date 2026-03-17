import math


def rendu_monnaie_TD(pieces, s, m):
    if s == 0:
        return 0

    elif m[s] > 0:        # already computed
        return m[s]

    else:
        nombre_min = math.inf
        for p in pieces:
            if p <= s:
                nombre_pieces = 1 + rendu_monnaie_TD(pieces, s - p, m)
                if nombre_pieces < nombre_min:
                    nombre_min = nombre_pieces

        m[s] = nombre_min
        return nombre_min


# test
pieces = [2, 5, 10]
s = 11
m = [0] * (s + 1)

print(rendu_monnaie_TD(pieces, s, m))
