board = [
    "[1]", "[2]", "[3]",
    "[4]", "[5]", "[6]",
    "[7]", "[8]", "[9]"
]

def print_borad(borad):
    for i in range(0, len(board), 3):
        print("  |  ". join(board[i:i + 3]))
        if i < (len(board) - 3):
            print("-----+-------+-----")