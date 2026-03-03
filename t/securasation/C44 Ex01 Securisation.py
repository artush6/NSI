d = {chr(i+65): chr((i+13) % 26+65) for i in range(26)}
print(d)

message = "BONNE ANNEE ET BONNE SANTE"

#### Chiffrement ####

"""A FAIRE"""

message_chiffre = ""

for lettre in message:
    message_chiffre += d.get(lettre, lettre)

print(message_chiffre)

#### Déchiffrement ####

"""A FAIRE"""

message_dechiffre = ""

for lettre in message_chiffre:
    message_dechiffre += d.get(lettre, lettre)

print(message_dechiffre)
