def an(y, s):
    count = 0
    step = 1
    for i in y:
        count += s * i * step
        step *= 10
    return count


def main():
    v = '55'
    u = '1175'
    if len(v) < len(u):
        v = [int(i) for i in v]
        u = int(u)
        print(an(v, u))
    else:
        u = [int(i) for i in u]
        v = int(v)
        print(an(u, v))


if __name__ == "__main__":
    main()
