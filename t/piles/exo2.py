class Pile:
    def __init__(self):
        self.lst = []   # start with empty stack

    def est_vide(self):
        return len(self.lst) == 0

    def empiler(self, item):
        self.lst.append(item)

    def depiler(self):
        assert not self.est_vide(), "Pile vide !"
        return self.lst.pop()

    def sommet(self):
        assert not self.est_vide(), "Pile vide !"
        return self.lst[-1]

    def taille(self):
        return len(self.lst)


def bien_parenthese(string: str) -> bool:
    p = Pile()

    for char in string:
        if char == "(":
            p.empiler(char)
        elif char == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()

    if p.est_vide():
        return True
    else:
        return False


print(bien_parenthese("(5*3)+[7*6]"))
print(bien_parenthese("(...(..(..)...)"))
print(bien_parenthese("(..(..)..)"))
