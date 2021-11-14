arr = ['!', 6, 3, 0, 2, 'watch', 9, 'villains']



def yes_no(arr):
    arr1 = []
    arr2 = []
    if len(arr) == 0:
        return []
    for i in range(0, len(arr), 2):
        arr1.append(arr[i])
    for i in range(1, len(arr), 2):
        arr2.append(arr[i])
    if len(arr2) == 2:
        return arr1 + arr2[::-1]
    else:
        arr1.append(arr2[0])
        arr2.pop(0)
        return arr1 + yes_no(arr2)


print(yes_no(arr))
