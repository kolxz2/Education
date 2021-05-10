"""
переопределение м пергрузка методов, абстрактные методы
"""


class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    # метод проверяет принадлежность аргументов к числам
    def isDigit(self):
        if (isinstance(self.__x, int) or isinstance(self.__x, float) and
                isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        else:
            return False

    # метод проверяет принадлежность аргументов к целым числам
    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        else:
            return False

    # создаём абстрактный метод, чтобы подсвечивать ошибку, ели не во всех
    # дочерних классах будет создан этот метод. Когда создаёться дочерний
    # класс, с таим же название, то он переозначаться
    def draw(self):
        raise NotImplementedError('В дочернем классе должен быть метод draw')


class Prop:
    def __init__(self, sp: Point, eps: Point, color: str = 'red',
                 width: int = 1):
        self._sp = sp
        self._eps = eps
        self._color = color
        self._width = width

    # прописываем сеттер для переобозначения новых значений принимает
    # аргументы из дочернего класса которяе вывывают метод проверки на числа
    def setCords(self, sp, eps):
        if sp.isDigit() and eps.isDigit():
            return sp, eps
        else:
            print('Не числа')


class Line(Prop):
    def draw(self):
        print(f" Drow Line: {self._sp}, {self._eps}, {self._color}, "
              f"{self._width}")

    # создаём приватный метод которым пользуемся только внутри класса
    # для для проверки числа на int
    def __setOneCords(self, sp):
        if sp.isInt():
            self._sp = sp
        else:
            print('Координаты должны быть целыми числами')

    # создаём приватный метод которым пользуемся только внутри класса
    # для для проверки чисел на int
    def __setTowCords(self, sp, eps):
        if sp.isInt() and eps.isInt():
            self._sp = sp
            self._eps = eps
        else:
            print('Координаты должны быть целыми числами')

    # ереопределеяем класс сеттер для проверки только int
    def setCords(self, sp: Point, eps: Point = None):
        if eps is None:
            self.__setOneCords(sp)
        else:
            self.__setTowCords(sp, eps)


class Rect(Prop):
    def draw(self):
        print(f" Drow Rect: {self._sp}, {self._eps}, {self._color}, "
              f"{self._width}")


class Ellipse(Prop):
    def draw(self):
        print(f" Drow Ellipse: {self._sp}, {self._eps}, {self._color}, "
              f"{self._width}")


lowLin = Line(Point(1, 5), Point(5, 9))
lowLin.draw()
lowLin.setCords(Point(1, 5), Point(5, 9))
lowLin.draw()
figs = []
figs.append(Line(Point(1, 2), Point(5, 8)))
figs.append(Rect(Point(1, 2), Point(5, 8)))
figs.append(Ellipse(Point(1, 2), Point(5, 8)))
for figure in figs:
    figure.draw()
