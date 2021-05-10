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
        # создаём приватную переменную в классе она создаётся с
        # перфиксом этого класса и среди локальных свойств другого
        # класса мы увидим эту переменную, но уже с перфиком этого
        # класса _Prop__width
        self.__width = width
    # геттер для работы с приватным методом
    def getWidth(self):
        return self.__width


# реализуем наследлывание, чтобы нп повторяться
class Line(Prop):
    def __init__(self, *args):
        print('Переопределён конструктор Line')
        # в классе не существует нужных переменных
        # поэтому мы явно указываем, из какого класса нужно наследовать НО
        # это порожает другие ошибки
        # Prop.__init__(self, *args)
        super().__init__(*args)
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
        print(f"рисование линии: {self._sp}, {self._ep}, {self.getWidth()}, {self._color}")


class Rect(Prop):
    """
    def __init__(self, spe: Point, ep: Point, color='red', width=1):
        self._sp = spe
        self._ep = ep
        self._color = color
        self._width = width
        """
    def __init__(self, *args):
        print('Переопределён конструктор Rect')
        # в классе не существует нужных переменных
        # поэтому мы явно указываем, из какого класса нужно наследовать НО
        # это порожает другие ошибки
        # Prop.__init__(self, *args)
        super().__init__(*args)

    def drowLine(self):
        print(f"рисование линии: {self._sp}, {self._ep}, {self.getWidth()}, {self._color}")


sp = Line(Point(9, 8), Point(7, 8))
kub = Rect(Point(1, 2), Point(5, 6))
sp.drowLine()
kub.drowLine()
