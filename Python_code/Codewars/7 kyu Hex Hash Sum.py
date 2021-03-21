def hex_hash(code):
    count = 0
    for i in code:
        d = [x for x in str(hex(ord(i)))]
        if 'x' in d:
            d.remove('x')
        if 'a'in d:
            d.remove('a')
        if 'b' in d:
            d.remove('b')
        if 'c' in d:
            d.remove('c')
        if 'd' in d:
            d.remove('d')
        if 'e' in d:
            d.remove('e')
        if 'f' in d:
            d.remove('f')
        d = [int(x) for x in d]
        count += sum(d)
    return count


print(hex_hash('Yo'))
"""
def hex_hash(code):
    return sum(int(d) for c in code for d in hex(ord(c)) if d.isdigit())
"""