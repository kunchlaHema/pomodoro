# to create th sudoko board
def user_input():
    row = int(input("enter the row in which you want to place the num: "))
    col = int(input("enter the col in which you want to place the num: "))
    num = int(input("enter the num which you want to place: "))
    return row, col, num

def create_board():
     return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

def display_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
    for _ in range(9):
        if num == board[row][_]:
            return False
    for _ in range(9):
        if num == board[_][col]:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def update_board(board, row, col, num):
    board[row][col] = num

def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True

def loop_of_game():
    board = create_board()
    while not is_complete(board):
        display_sudoku(board)
        row, col, num = user_input()
        if is_valid(board, row, col, num):
            update_board(board, row, col, num)
            print("Valid move!")
        else:
            print("Invalid move, try again.")
    print("Congratulations, you completed the Sudoku!")
    display_sudoku(board)

# Start the game
loop_of_game()




















