string = "hi())("


def valid_parentheses(string):
    mas = []
    for i in string:
        mas.append(i)
    return mas


print(valid_parentheses(string))