arr = [1, 6, 7, 9, 11]


def mine(arr):
    result = 0
    flag = True
    for i in arr:
        while flag:
            if i != 6:
                result += i
                break
            else:
                flag = False
        while not flag:
            if i != 9:
                break
            else:
                flag = True
                break
    return result


print(mine(arr))
