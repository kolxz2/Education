# Практика. Класс Point(x, y)
# dry (don't repeat yourself) - убирать пос=вторяяющие строчки кода
# Импортируем только квадатный корень
from math import sqrt


# создаём класс с тосками
class Point:
    # создаем список в котором будем гранить адрес новой созданной переменной
    # через 'Point.list_point[...].x' можно обращаться к значениям конкретной переменной
    list_point = []

    # создаём init для создания первых данных у точки
    def __init__(self, cord_x=0, cord_y=0):
        # вызываем метод 'move_to' которому передаём параметры cord_x=0, cord_y=0
        self.move_to(cord_x, cord_y)
        # Через 'append' добавляем адресс нового элемента в список
        Point.list_point.append(self)

    # прописывае метод для изменения координат точки
    def move_to(self, cord_x, cord_y):
        # присваеваем атрибутам объекта новые значения
        self.x = cord_x
        self.y = cord_y

    # обнуляем координаты точки
    def go_home(self):
        self.move_to(0, 0)

    # выводим коордиднаты
    def show_point(self):
        print(f'Точка с координатами ({self.x},{self.y})')

    # расчитывае длину медлу точками, передаём в метод новый парамерт (точку)
    def calc_distance(self, another_point):
        # является ли указанный объект экземпляром указанного класса возвращает True/False
        if not isinstance(another_point, Point):
            #  через raise выводим ошибку в консоль
            raise ValueError('Вы передали не верный аргумент')
        # если всё нас устраивает, то расчитывае длинну
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)
