pioints = [(13, 13), (13, 478), (479, 13), (479, 478)]
print(set(pioints[0]+pioints[1]+pioints[2]+pioints[3]))

def is_square(points):
    if len(points) != 4:
        return False
    else:
        points.sort()
        one = (points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2
        two = (points[1][0] - points[2][0]) ** 2 + (points[1][1] - points[2][1]) ** 2
        three = (points[2][0] - points[3][0]) ** 2 + (points[2][1] - points[3][1]) ** 2
        thor = (points[3][0] - points[0][0]) ** 2 + (points[3][1] - points[0][1]) ** 2
        if one == 0 or two == 0 or thor == 0 or three == 0:
            return False
        else:
            return one == three and thor == two

print(is_square(pioints))
