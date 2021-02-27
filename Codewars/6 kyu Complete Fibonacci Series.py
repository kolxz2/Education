n = 6


def fibonacci(n):
    f = 0
    s = 1
    x = [0, 1]
    if n <= 1:
        return []
    else:
        for i in range(2, n):
            next = f + s
            x.append(next)
            f = s
            s = next
    return x


print(fibonacci(n))
