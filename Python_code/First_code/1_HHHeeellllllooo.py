# -> Hello
# >> HHHeeellllllooo
phrase = input("Enter phrase: ")


def umnozdh(phrase):
    result = ""
    for i in phrase:
        result += i * 3
    return result


print(umnozdh(phrase))
