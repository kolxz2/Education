"""
свои классы исключений и итераторы
"""


class CordError(Exception):
    pass


class ImageXIterator:
    def __init__(self, img, y: int):
        self.__limit = img.width
        self.__y = y
        self.__img = img
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration
        self.__x += 1
        return self.__img[self.__x-1, self.__y]


class ImageYIterator:
    def __init__(self, img):
        self.__limit = img.height
        self.__img = img
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration
        self.__y += 1
        return ImageXIterator(self.__img, self.__y-1)


class Image:
    def __init__(self, width, height, background='_'):
        self.__background = background
        """
        в pixels self.__pixels[(x,y)] = color где х и у являються ключами
        """
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, height):
        self.__width = height

    def __checkCords(self, coord):
        # кординаты должны быть карьежем и дленак картежа не
        # должна быть больше 2
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CordError('Координаты не верны')
        # координаты должны попасть внутрь изображения
        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            raise CordError('Координаты выходят за пределы картинки')

    def __setitem__(self, coord, color):
        self.__checkCords(coord)
        if color == self.__background:
            self.__pixels.pop(coord, self.__background)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)

    def __getitem__(self, coord):
        self.__checkCords(coord)
        # с помощь гета получаем пиксель с данной координатой
        return self.__pixels.get(coord, self.__background)

    def __iter__(self):
        return ImageYIterator(self)


img = Image(4, 4)
img[1, 1] = '*'; img[2, 1] = '*'; img[3, 1] = '*'
for y in range(img.height):
    for x in range(img.width):
        print(img[x, y], sep=' ', end='')
    print()

for row in img:
    for pixel in row:
        print(pixel, sep=" ", end='')
    print()
