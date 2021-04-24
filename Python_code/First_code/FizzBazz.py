list_num = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        list_num.append(i)
        list_num.append("FizzBazz")
    elif i % 3 == 0:
        list_num.append(i)
        list_num.append("Fizz")
    elif i % 5 == 0:
        list_num.append(i)
        list_num.append("Bazz")
print(list_num)
