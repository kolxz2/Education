"""
переопределение м пергрузка методов, абстрактные методы
"""


class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Prop:
    def __init__(self, sp: Point, eps: Point, color: str = 'red',
                 width: int = 1):
        self._sp = sp
        self._eps = eps
        self._color = color
        self._width = width


class Line(Prop):
    def drawLine(self):
        print(f" Drow Line: {self._sp}, {self._eps}, {self._color}, "
              f"{self._width}")


lowLin = Line(Point(1, 5), Point(5, 9))
