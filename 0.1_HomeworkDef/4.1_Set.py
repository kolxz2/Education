num_list = input("Enter nums")


def main(num_list):
    x = []
    for i in num_list:
        if i not in x:
            x.append(i)
    return x


print(main(num_list))
