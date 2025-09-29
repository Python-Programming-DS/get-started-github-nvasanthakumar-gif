# Author: Nitishwar Vasntha Kumar
# Date: 24 September 2025
# Connect Four game played in terminal.
# Two players alternate placing tokens ('X' and 'O') by specifying column and row.
# The first player to get four in a row horizontally, vertically, or diagonally wins.

ROWS = 6
COLS = 7
COL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def resetBoard():
    # create empty 6x7 board
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def printBoard(board):
    # display board with row numbers and column letters
    for r in range(ROWS, 0, -1):
        print(f"| {r} |", end="")
        for c in range(COLS):
            print(f" {board[r-1][c]} |", end="")
        print()
    print("   " + "-" * (COLS * 4 + 1))
    print("    ", end="")
    for letter in COL_LETTERS:
        print(f"{letter:^4}", end="")
    print("\n")

def availablePositions(board):
    # return list of next available positions in each column
    positions = []
    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == ' ':
                positions.append(f"{COL_LETTERS[c]}{r+1}")
                break  
    return positions

def validateEntry(board, pos):
    # check if entered position is valid and available
    if len(pos) != 2:
        return False
    col_letter = pos[0].lower()
    row_char = pos[1]
    if col_letter not in COL_LETTERS:
        return False
    if not row_char.isdigit():
        return False
    row = int(row_char)
    if row < 1 or row > ROWS:
        return False
    col = COL_LETTERS.index(col_letter)
    for r in range(ROWS):
        if board[r][col] == ' ':
            lowest = r + 1  # row number (1-based)
            break
    else:
        # Column full
        return False
    return row == lowest

def placeToken(board, pos, token):
    # place token in valid board position
    col = COL_LETTERS.index(pos[0].lower())
    row = int(pos[1]) - 1
    board[row][col] = token

def checkWin(board, token):
    # Return True if token has connected four in any direction
    # Horizontal check
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == token for i in range(4)):
                return True
    # Vertical check
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == token for i in range(4)):
                return True
    # Diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == token for i in range(4)):
                return True
    # Diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == token for i in range(4)):
                return True
    return False

def checkFull(board):
    # check if the board is full
    return all(board[ROWS-1][c] != ' ' for c in range(COLS))

def playGame():
     # main game loop
    while True:
        board = resetBoard()
        print("New game: X goes first.\n")
        printBoard(board)
        tokens = ['X', 'O']
        turn = 0

        while True:
            token = tokens[turn % 2]
            print(f"{token}'s turn.")
            available = availablePositions(board)
            print(f"Available positions are: {available}")
            pos = input("Please enter column-letter and row-number (e.g., a1): ").strip()
            if not validateEntry(board, pos):
                print("Invalid position! Make sure to pick from the available positions.")
                continue
            placeToken(board, pos, token)
            print("Thank you for your selection.\n")
            printBoard(board)

            if checkWin(board, token):
                print(f"{token} IS THE WINNER!!!\n")
                break
            if checkFull(board):
                print("It's a draw! The board is full.\n")
                break
            turn += 1

        again = input("Another game (y/n)? ").strip().lower()
        if again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    playGame()
