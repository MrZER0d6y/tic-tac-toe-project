WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

def occupied_cell(board, player_turn, choice):
    if len(board[choice]) == 4:
        print(f"\nCell is already occupied by {player_turn}, choose another cell.")
        return True
    return False

def user_choice(board, player_turn):
    valid_user_choice = False
    while not valid_user_choice:
        try:
            choice = int(input(f"Player {player_turn}, choose a cell (1-9): "))
        except ValueError:
            print("\nCell must be integer.")
            continue

        if choice < 1 or choice > 9:
            print("\nCell must be between 1 to 9.")
            continue
        
        choice -= 1
        if occupied_cell(board, player_turn, choice):
            continue

        valid_user_choice = True
    return choice

def winning(board, player_turn, print_borad):
    for line in WINNING_LINES:
        if player_turn in board[line[0]] and player_turn in board[line[1]] and player_turn in board[line[2]]:
            print("")
            print_borad(board)
            print(f"Player {player_turn} wins!")
            return True
    return False

def mark_cell(board, player_turn, choice):
    board[choice] += str(player_turn)
    return

def next_turn(player_turn):
    if player_turn == "X":
        return "O"
    return "X"

def draw(board, print_board):
    print("")
    print_board(board)
    print("It's a draw!")
    return