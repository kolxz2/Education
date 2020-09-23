board = range(1, 10)


def dsiplay_board():
    print("__ __ __")
    for i in range(3):
        print(board[0 + i * 3], " | ", board[1 + i * 3], " | ", board[2 + i * 3])
        print("_ _ _ ")


print(dsiplay_board())
