palindrom = input("Enter word: ")


def control(palindrom):
    palindrom = palindrom.replace(' ', '')
    palindrom = palindrom.lower()
    return palindrom == palindrom[::-1]


print(control(palindrom))
