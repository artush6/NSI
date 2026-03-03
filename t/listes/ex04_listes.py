"""
Écrire une fonction qui prend en paramètres deux listes val et coeff de même longueur puis qui calcule la moyenne des valeurs de la liste val pondérée par les coefficients de la liste coeff.
Exemple :  si val=[12.5, 13.6, 18.4, 9.7] et coeff=[2, 3, 5, 4], la moyenne pondérée vaut :
( 12,5×2+13,6×3+ 18,4×5+ 9,7×4)
(2+ 3+5+ 4 )                    ≃14,043
"""


def main(val: list, coeff: list) -> float:
    result = 0
    top = 0
    bottom = 0

    # use zip to loop over values and coefficients together
    for v, c in zip(val, coeff):
        top += v * c

    for j in coeff:
        bottom += j

    result = top / bottom
    print(result)
    return result


main([12.5, 13.6, 18.4, 9.7], [2, 3, 5, 4])
