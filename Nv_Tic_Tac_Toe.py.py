"""
Tic-Tac-Toe
Author: Nitishwar Vasantha Kumar
Date: Sept 24, 2025

A simple two-player Tic-Tac-Toe game played in the terminal.
Players take turns placing X or O until someone wins or the board is full.
"""

def print_board(board):
     # print grid with row/column numbers for reference
     # display board with row/column indices
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:  # no line after last row
            print("  -----------")
    print()

def reset_board():
    # create empty 3x3 board
    return [[" " for _ in range(3)] for _ in range(3)]

def is_valid_move(row, col, board):
    # check if cell is in range and empty
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def board_full(board):
    # check if all cells filled
    return all(cell != " " for row in board for cell in row)

def check_winner(board, player):
    # check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        # check columns
        if all(board[r][col] == player for r in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def game_state(board, player):
    # return current state: win, tie, or playing
    if check_winner(board, player):
        return "win"
    if board_full(board):
        return "tie"
    return "playing"

def get_player_move(player, board):
    # prompt user for valid row,col input
    while True:
        print(f"\n{player}'s turn.")
        print(f"Where do you want your {player} placed?")
        print("Please enter row number and column number separated by a comma.")
        move = input().strip()
        try:
            row_str, col_str = move.split(",")
            row, col = int(row_str), int(col_str)
            print(f"You have entered row #{row}\nand column #{col}")
        except (ValueError, IndexError):
            print("Invalid entry: try again.")
            print("Row & column numbers must be either 0, 1, or 2.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid entry: try again.")
            print("Row & column numbers must be either 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("That cell is already taken.")
            print("Please make another selection.")
            continue
        return row, col

def main():
    print("Welcome to Tic-Tac-Toe!")
    board = reset_board()
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_move(current_player, board)
        board[row][col] = current_player
        state = game_state(board, current_player)

        if state == "win":
            print_board(board)
            print(f"{current_player} IS THE WINNER!!!")
            break
        elif state == "tie":
            print_board(board)
            print("DRAW! NOBODY WINS!")
            break
        # switch player
        current_player = "O" if current_player == "X" else "X"

    again = input("\nAnother game? Enter Y or y for yes.\n").strip().lower()
    if again == "y":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
