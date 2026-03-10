def hanoi(n, tige_depart, tige_arrivee, tige_trois):
    if n == 1:
        print("Disque 1 :", tige_depart, "->", tige_arrivee)
    else:
        hanoi(n-1, tige_depart, tige_trois, tige_arrivee)
        print("Disque", n, ":", tige_depart, "->", tige_arrivee)
        hanoi(n-1, tige_trois, tige_arrivee, tige_depart)

hanoi(3, "A", "C", "B")

"""
Disque 1 : A -> C
Disque 2 : A -> B
Disque 1 : C -> B
Disque 3 : A -> C
Disque 1 : B -> A
Disque 2 : B -> C
Disque 1 : A -> C
"""