from borad import *
from game import *

def main():
    finish = False
    player_turn = "X"
    remaining_cells = 9

    while not finish:
        print_borad(board)
        choice = user_choice(board, player_turn)
        mark_cell(board, player_turn, choice)

        if winning(board, player_turn, print_borad):
            finish = True
            continue

        remaining_cells -= 1
        if remaining_cells == 0:
            draw(board, print_borad)
            finish = True
            continue

        player_turn = next_turn(player_turn)
        print("")
    return 0

if __name__ == "__main__":
    main()