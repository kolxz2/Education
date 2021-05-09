"""
B питоне всё являеться объектом. В наследовании мы создаём Дочерний класс
на основе Базового. Любой класс в Python не явно наследуеться из класса
object
"""


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x},{self.__y})'


class Prop:
    def __init__(self, spe: Point, ep: Point, color='red', width=1):
        self._sp = spe
        self._ep = ep
        self._color = color
        self._width = width


# реализуем наследлывание, чтобы нп повторяться
class Line(Prop):
    """
    # через двоеточие указываем то что ожидаем получить при ввводе,
    # но вводить можно всё что угодно
    def __init__(self, spe: Point, ep: Point, color='red', width=1):
        self._sp = spe
        self._ep = ep
        self._color = color
        self._width = width
    """

    # создаём метод который преобразует наши данные в строковые переменные

    def drowLine(self):
        print(f"рисование линии: {self._sp}, {self._ep}, {self._width}, {self._color}")


class Rect(Prop):
    """
    def __init__(self, spe: Point, ep: Point, color='red', width=1):
        self._sp = spe
        self._ep = ep
        self._color = color
        self._width = width
        """

    def drowLine(self):
        print(f"рисование линии: {self._sp}, {self._ep}, {self._width}, {self._color}")


sp = Line(Point(9, 8), Point(7, 8))
kub = Rect(Point(1, 2), Point(5, 6))
sp.drowLine()
kub.drowLine()
