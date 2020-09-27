cart1 = int(input("Enter nums: "))
cart2 = int(input("Enter nums: "))
cart3 = int(input("Enter nums: "))


def sucaunt(cart1, cart2, cart3):
    if sum([cart1, cart2, cart3]) <= 21:
        return sum([cart1, cart2, cart3])
    elif 11 in [cart1, cart2, cart3] and sum([cart1, cart2, cart3]) <= 31:
        return sum([cart1, cart2, cart3]) - 10
    else:
        return "Brash"


print(sucaunt(cart1, cart2, cart3))
