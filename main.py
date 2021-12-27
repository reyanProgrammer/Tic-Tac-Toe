import numpy as np


def is_win(board):
    wc = [whose_turn, whose_turn, whose_turn]
    if board[0:3] == wc:
        return False
    else:
        return True


def which_win(board):
    wc = [whose_turn, whose_turn, whose_turn]

    if board[0:3] == wc:
        print(f"Player {whose_turn} wins")

    # if board[i][0:2] == ["Y", "Y", "Y"]:
    #     print("Player2 wins")


def printboard(board: list):
    for item in board:
        print(item, end=" ")
        if item == 3:
            print()
        elif item == 6:
            print()
        elif item == 8:
            print()
    print()


board = [1, 2, 3, 4, 5, 6, 7, 8
         ]

whose_turn = "X"
game_over = is_win(board)

while game_over:

    printboard(board)

    print("IT'S X turns")
    whose_turn = "X"
    player1NO = int(input("PLAYER1: Chose where to put X (Number) "))

    if not board[player1NO-1] == "X" or "Y":
        board[player1NO-1] = "X"
    else:
        print("You can't put X ")

    which_win(board)
    game_over = is_win(board)

    printboard(board)
    print("IT'S Y turns")
    whose_turn = "Y"

    player2NO = int(input("PLAYER2: Chose where to put Y (Number) "))

    if not board[player2NO-1] == "X" or "Y":
        board[player2NO-1] = "Y"
    else:
        print("You can't put Y ")
    printboard(board)
    which_win(board)
    game_over = is_win(board)
