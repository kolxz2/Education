list_my = input("Enter your phrase: ")


def main(list_my):
    trans_list = [i for i in list_my]
    count = {"upper": 0, "lower": 0}
    for i in trans_list:
        if i.isupper():
            count["upper"] += 1
        elif i.islower():
            count["lower"] += 1
        else:
            pass
    print("Исходная строка: ", list_my)
    print("Количество символов в нижнем регистре: ", count["lower"])
    print("Количество символов в верхнем регистре: ", count["upper"])


main(list_my)
