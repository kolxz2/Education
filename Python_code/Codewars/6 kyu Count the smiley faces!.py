arr = [':D',':~)',';~D',':)']

def count_smileys(arr):
    arr1 = [i for i in arr if 'D' in i or ')' in i]
    arr2 = [i for i in arr1 if ':' in i or ';' in i]
    arr3 = []
    for i in arr2:
        if len(i) == 2:
            arr3.append(i)
        else:
            if '-' in i or '~' in i:
                arr3.append(i)
    return len(arr3)