class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Style:
    def __init__(self, color='red', width=1, *args):
        print('Конструктор Style')
        self._color = color
        self._width = width
        super().__init__(*args)


class Pos:
    def __init__(self, sp: Point, eps: Point, *args):
        print('Конструктор Pos')
        self._sp = sp
        self._eps = eps
        super().__init__(*args)


class Line(Pos, Style):
    def drow(self):
        print(f'Drow line: {self._sp}, {self._eps}, {self._color}, {self._width}')


lowLin = Line(Point(1, 5), Point(5, 9))
lowLin.drow()
