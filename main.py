from borad import *
from game import *

def main():
    player_turn = "X"

    for _ in range(9):
        print_borad(board)
        choice = user_choice(board, player_turn)
        mark_cell(board, player_turn, choice)

        if winning(board, player_turn, print_borad):
            finish = True
            continue

        player_turn = next_turn(player_turn)
        print("")

    draw(board, print_borad)
    return 0

if __name__ == "__main__":
    main()