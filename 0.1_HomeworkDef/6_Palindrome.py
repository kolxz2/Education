palindrom = input("Enter word: ")


def control(palindrom):
    del_spase = palindrom.replace(' ', '')
    pa_list = [i for i in del_spase]
    turn = pa_list[::-1]
    for i in pa_list:
        for j in turn:
            if i == j:
                return True
            else:
                return False


print(control(palindrom))
