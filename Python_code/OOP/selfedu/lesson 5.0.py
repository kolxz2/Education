class Point:
    """
    count = 0 # статическое свойство при его изменении Point.count = 10
    во всех экземплярах значение count будет изменено
    """
    __count = 0

    def __init__(self,y=0 ,x=0):
        Point.__count += 1
        # сейчас создаёл локальные свойства для экземпляров
        self.cordx = x
        self.cordy = y

    # создали статический метод который работает только с атрибутами класса Point
    @staticmethod
    def getCount(): # так как метод статический, то self не нужен
        return Point.__count


pt = Point()
pt2 = Point()
Point.count = 10
# без указания статического метода в Point в  скобочках надо указать любой параметр
Point.getCount()
print(pt.count ,pt2.getCount())
