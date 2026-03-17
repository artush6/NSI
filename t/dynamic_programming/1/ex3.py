import math


def rendu_monnaie_BU(pieces, s):
    m = [math.inf] * (s + 1)
    m[0] = 0  # base case

    for n in range(1, s + 1):
        for p in pieces:
            if n % p == 0:
                m[n] = n // p
            if p <= n:
                m[n] = min(m[n], 1 + m[n - p])

    return m[s]


# tests
print(rendu_monnaie_BU([2, 5, 10], 11))  # 4
print(rendu_monnaie_BU([2, 5, 10], 16))  # 3
print(rendu_monnaie_BU([2, 5, 10], 21))  # 3
