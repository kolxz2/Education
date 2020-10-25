my_string = input("Enter text: ")

def count_lettering(my_string):
    count_low = 0
    count_high = 0
    string_dev = [i for i in my_string]
    for j in string_dev:
        if j.isupper():
            count_high += 1
        elif j.islower():
            count_low += 1
    return count_low, count_high


letterMin, letterMax = count_lettering(my_string)
print("Колличество символов в верхнем регистре: {}".format(letterMax))
print("Колличество символов в нижнем регистре: {}".format(letterMin))
