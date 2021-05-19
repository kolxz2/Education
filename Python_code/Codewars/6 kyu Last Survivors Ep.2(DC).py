string = 'abaa'
final = []

def last_survivors(string):
    strings = [i for i in string]
    count = 0
    mass = []
    final = []
    finish = []
    for i in strings:
        if i == 'z' and i in mass:
            mass = delete(mass, i)
            finish.append('a')
        elif i in mass:
            mass = delete(mass, i)
            finish.append(chr(ord(i) + 1))
        else:
            mass.append(i)
    newly = ''.join(mass + finish)
    newly = [i for i in newly]
    final = newly
    for i in newly:
        sym = i
        newly.pop(count)
        if sym in newly:
            newly.append(i)
            newly = last_survivors(newly)
        count += 1
    return final


def delete(massiv, elem):
    count = 0
    for i in massiv:
        if i == elem:
            massiv.pop(count)
        count += 1
    return massiv


print(last_survivors(string))
