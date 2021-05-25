"""
Итерируеммость класса
"""


class MyIter:
    def __init__(self, limit):
        self.__limit = limit

    # показываем что объект итерируется, позволяет инициализировать
    def __iter__(self):
        self.__num = 0
        return self

    # необходим для вывода значения итераций
    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration
        self.__num += 1
        return self.__num


it = MyIter(10)
for i in it:
    print(i)
