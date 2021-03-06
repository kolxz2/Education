from functools import reduce
a = [3, 2, 5]
b = [1, 4, 4]


def find_difference(a, b):
    x = reduce(lambda x, y: x*y, [3, 2, 5])
    y = reduce(lambda x, y: x*y, b)
    return abs(x - y)

print(find_difference(a, b))
