list_count = input("Entrer array: ")


def transformation(list_count):
    del_spase = list_count.replace(' ', '')
    briliant_trans = [i for i in del_spase]
    result = [int(i) for i in briliant_trans]
    return result


num = transformation(list_count)
print(num)


def main_fun(num):
    count = 0
    for i in num:
        count += i
    return count


print(main_fun(num))
