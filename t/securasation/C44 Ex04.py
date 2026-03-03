def rsa(message, e, n):
    '''Exemple : message='RSA', ord('R')=82 qui est le code ascii du caractère 'R', ord('S')=83...
     On concatène ensuite les chaînes de caractères : '82'+'83'+'65'='828365'
     On transforme cette chaîne de caractères en l'entier 828365
     On retourne le reste de la division euclidienne de m**e par n'''
    # TODO
    m = ""
    for letter in message:
        m += str(ord(letter))

    number = int(m)
    return pow(number, e, n)


def cle_privee(e, f):
    '''on initialise la clef privée d à 1
    Tant que d est stictement inférieure à f, si le reste de la division euclidienne de ed par f est égal à 1,
    on retourne d, sinon on incrémente d de 1'''
    # TODO
    d = 1
    while d < f:
        if (e * d) % f == 1:
            return d
        else:
            d += 1


def dechiffrement(x, d, n):
    nb = 1
    for i in range(d):
        nb = (nb*x) % n
    return nb


def dechiff_final(nb):
    '''Dans l'exemple : nb=828365
    On transforme nb en une chaîne de caractères : '828365'
    chr(82)='R',chr(83)='S',...
    On retourne le message déchiffré'''
    # TODO
    string = str(nb)
    m = ""
    for i in range(0, len(string), 2):
        ascii_code = int(string[i:i+2])
        m += chr(ascii_code)

    return m


### TEST ###

p = 6991
q = 7529
n = p*q
f = (p-1)*(q-1)
e = 23
message = 'RSA'

# à décocher à la question 2 pour tester la fonction rsa.
"""x = rsa(message,e,n)
print(x)"""

# à décocher à la question 3 pour tester la fonction cle_privee.
"""d = cle_privee(e,f)
print(d)"""

# à décocher à la question 4 pour tester la fonction dechiffrement.
"""nb=dechiffrement(x, d, n)
print(nb)"""

# à décocher à la question 5 pour tester la fonction dechiff_final.
"""print(dechiff_final(nb))"""
