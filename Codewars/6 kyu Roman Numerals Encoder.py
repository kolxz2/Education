def solution(n):
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    thousand = int(n / 1000)
    five_hundred = int((n - thousand * 1000) / 500)
    one_hunred = int((n - thousand * 1000 - five_hundred * 500) / 100)
    fify = int((n - thousand * 1000 - five_hundred * 500 - one_hunred * 100) / 50)
    ten = int((n - thousand * 1000 - five_hundred * 500 - one_hunred * 100 - fify * 50) / 10)
    five = int((n - thousand * 1000 - five_hundred * 500 - one_hunred * 100 - fify * 50 - ten * 10) / 5)
    one = int((n - thousand * 1000 - five_hundred * 500 - one_hunred * 100 - fify * 50 - ten * 10 - five * 5) / 1)
    return thousand, five_hundred, one_hunred, fify, ten, five, one


print(solution(2345))