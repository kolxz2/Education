list_enter = input("Enter arrms: ")


def main(list_enter):
    create_nums = [i for i in list_enter]
    transform = set(create_nums)
    return transform


print(main(list_enter))
