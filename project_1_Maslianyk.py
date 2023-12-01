from random import randrange

def display_board(board):
    line = "+---" * 3 + "+"
    for row in board:
        print(line)
        for cell in row:
            print(f"| {cell} ", end="")
        print("|")
    print(line)

def enter_move(board):
    move = int(input("Enter your move: "))
    if move < 1 or move > 9:
        print("Incorrect input. Enter a number from 1 to 9.")
        return False

    for row in range(3):
        for column in range(3):
            if board[row][column] == str(move):
                board[row][column] = "O"
                return True

    print("This cell is already occupied. Enter another number.")
    return False

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] != "X" and board[row][column] != "O":
                free_fields.append((row, column))
    return free_fields

def victory_for(board, sign):
    for row in range(3):
        if all(cell == sign for cell in board[row]):
            return True

    for column in range(3):
        if all(board[row][column] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, column = free_fields[randrange(len(free_fields))]
        board[row][column] = "X"

def start():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

    display_board(board)

    while True:
        if not enter_move(board):
            continue

        display_board(board)

        if victory_for(board, "O"):
            print("You won!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            print("A draw!")
            break

        draw_move(board)
        print("Computer move:")
        display_board(board)

        if victory_for(board, "X"):
            print("The computer won!")
            break

start()
