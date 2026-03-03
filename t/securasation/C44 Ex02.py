# -*- coding:Utf-8 -*-

def chiffre(message, key):
    c = []
    n = len(message)
    m = len(key)
    j = 0
    for i in range(n):
        c.append(ord(message[i]) ^ ord(key[j]))
        j = (j+1) % m
    return c


def dechiffre(message, key):
    # À faire
    texte = ""
    m = len(key)
    j = 0
    for i in range(len(message)):
        texte += chr(message[i] ^ ord(key[j]))
        j = (j+1) % m
    return texte


message = "Bonjour, comment allez-vous ?"
cle = "mystère"
print(chiffre(message, cle))
