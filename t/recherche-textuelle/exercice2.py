def recherche_1caractere(lst: str, lettre: str) -> bool:
    for l in lst:
        if l == lettre:
            return True


print(recherche_1caractere('aacabacabaabaa', 'a'))
