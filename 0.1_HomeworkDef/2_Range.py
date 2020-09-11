while True:
    range_low = int(input("Enter low rage: "))
    range_high = int(input("Enter hight range: "))
    num = int(input("Enter num to compare: "))
    if range_low > range_high:
        print("Error range low bigger than highr")
    else:
        break


def main(num, range_low, range_high):
    if num <= range_high and num >= range_low:
        return True
    else:
        return False


if main(num, range_low, range_high):
    print("\n{} in the range across {} and {}".format(num, range_low, range_high))
else:
    print("\n{} not in the range across {} and {}".format(num, range_low, range_high))
