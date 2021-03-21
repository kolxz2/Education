num = 4554224


def descending_order(num):
    count = 0
    # x = sorted(list(str(num)))[::-1]
    x = sorted(str(num))[::-1]
    rez = int(10 ** (len(x) - 1))
    for i in x:
        count += int(i) * rez
        rez /= 10
   # s = str(num)
   # s = list(s)
   # s = sorted(s)
   # s = reversed(s)
   # s = ''.join(s)
   # return int(s)
    return int(count)


print(descending_order(num))
