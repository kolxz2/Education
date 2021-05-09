"""
класс синглитор - для которог можно создать только один экземпляр
"""
class Point:
    __count = 0
    __instanse = None

    # в new создаётся экземпляр класса, перегружая его мы контролируем кол-во
    # созданных экземпляров. cls ссылаеться на класс Point
    def __new__(cls, *args, **kwargs):
        # проеряем принадлежит ли __instanse классу Point, создаём класс
        if not isinstance(cls.__instanse, cls):
            # с помощью super создаём класс и его ссылку присваеваем __instanse
            cls.__instanse = super(Point, cls).__new__(cls)
        else:
            print('Класс создан')

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.countx = x
        self.county = y

    @staticmethod
    def getCount():
        return Point.__count

pt = Point()
pt2 = Point()
