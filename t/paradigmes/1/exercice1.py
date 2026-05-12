from math import sqrt


from math import sqrt


class Point:
    def __init__(self, initX, initY):
        self.__x = initX
        self.__y = initY

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_y(self, nouvelleValeur):
        if nouvelleValeur >= 0:
            self.__y = nouvelleValeur

    def translater(self, dx, dy):
        self.__x += dx
        if self.__y + dy >= 0:
            self.__y += dy

    def module(self):
        return sqrt(self.__x**2 + self.__y**2)

    def __str__(self):
        return f"({self.__x},{self.__y})"


print(p1)
d = p1.module()
print(d)
p1.translater(1, 1)
print(p1)
print(p1.get_x())
p1.y = 2
print(p1)
p1.y = -2
print(p1)
