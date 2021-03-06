size = 6


def multiplication_table(size):
    mas = []
    i_count = 1
    j_count = 1
    for i in range(size):
        mas.append([])
        for j in range(size):
            mas[i].append(i_count * j_count)
            j_count += 1
        i_count += 1
        j_count = 1
    return


print(multiplication_table(size))
""":cvar
def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]
"""