from string import ascii_letters

userString = input('Enter your world')


# Проверяем что пользователь ввёл толко одно слово и это слово на латинском
def validate(user_string):
    modify_str = []
    if all(map(lambda c: c in ascii_letters, user_string)):
        user_list = [i for i in user_string]
        for i in user_list:
            if i == ' ':
                return modify_str
            modify_str.append(i)
        return modify_str
    else:
        print('Not correct entering please use ASCII')


def split(mylist):
    return ''.join(mylist)


modification = split(validate(userString))
symbol = []


def pig_world(mod, sym):
    count = 0
    mod2 = list(mod)
    mod = [i for i in mod]
    dictionary = 'BCDFGHKLMNPQRSTVXX'
    for i in mod:
        if i.upper() in dictionary:
            sym.append(i)
            mod2.pop(count)
            return pig_world(mod2, sym)
        else:
            break
    return split(mod2), split(sym) + 'ay'


print(pig_world(modification, symbol))
