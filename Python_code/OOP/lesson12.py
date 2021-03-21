class Square:
    def __init__(self, s):
        self.side = s
        self.__aria = None

    @property
    def area(self):
        if self.__aria is None:
            print('Calculate aria')
            self.__aria = self.side ** 2
        return self.__aria
