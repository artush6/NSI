"""
  Écrire une fonction qui supprime les éléments en double d’une liste. Exemple :  
  liste de départ : L=[1,2,5,8,6,2,5,9,1,8,8]
  affichage :       [1,2,5,8,6,9]
"""


def main(lst: list) -> list:
    new_lst = []

    for item in lst:
        if item not in new_lst:
            new_lst.append(item)

    print(new_lst)
    return new_lst


main([1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8])
