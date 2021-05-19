"""
Способы перегрузки классов
__iadd__ / __eq__ / __add__ /
"""


class Clock:
    __Day = 8400  # число секунд в дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Секунды должны быть уелыми числами')

        self.__secs = secs % self.__Day

    def getFormatTime(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        return f'{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}'

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else '0' + str(x)

    def __getSecs(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый оператор должен быть от Clock')
        return Clock(self.__secs + other.__getSecs())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый оператор должен быть от Clock')
        self.__secs += other.__getSecs()
        return self

    def __eq__(self, other):
        return self.__secs == other.__getSecs()

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть срокой')

        if item == 'hour':
            return (self.__secs // 3600) % 24
        elif item == 'min':
            return (self.__secs // 60) % 60
        elif item == 'sec':
            return self.__secs % 60
        return "Невкрный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')
        if not isinstance(value, int):
            raise ValueError('Значение должно быть целым')
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        if key == 'hour':
            self.__secs = s + 60 * m + value * 3600
        if key == 'min':
            self.__secs = s + 60 * value + h * 3600
        if key == 'sec':
            self.__secs = value + 60 * m + h * 3600


c1 = Clock(100)
c2 = Clock(201)
c3 = c1 + c2
c2 += c1
print(c3.getFormatTime())
print(c2.getFormatTime())
if c2 == c3:
    print('Равны')
c1['hour'] = 10
print(c1['sec'], c1['min'], c1['hour'])
