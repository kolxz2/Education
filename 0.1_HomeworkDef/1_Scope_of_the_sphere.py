import math
radius = int(input("Enter radius: "))


def scope(radius):
    counter = (4/3 * math.pi) * radius ** 3
    return counter


print("Score = ", scope(radius))
