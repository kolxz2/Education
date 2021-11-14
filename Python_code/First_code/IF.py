string = 'zzzab'
final = []


def last_survivors(string):
    finish = []
    mass = []
    nevly = []
    strings = sorted(string)
    for i in strings:
        if i == 'z' and i in mass:
            mass = delete(mass, i)
            finish.append('a')
        elif i in mass:
            mass = delete(mass, i)
            finish.append(chr(ord(i) + 1))
        else:
            mass.append(i)
    string = ''.join(mass + finish)
    nevly = mass + finish
    for i, y in nevly, len(nevly) - 1:
        if i in nevly:
            pass
    return string


def delete(massiv, elem):
    count = 0
    for i in massiv:
        if i == elem:
            massiv.pop(count)
        count += 1
    return massiv


print(last_survivors(string))

