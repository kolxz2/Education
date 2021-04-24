pi = 3.14
n = input("Введите значение радиуса ")


def hren(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


if hren(n):
    fom_c = 4/3*pi*int(n)
    print(fom_c)
else:
    print("Not True")
