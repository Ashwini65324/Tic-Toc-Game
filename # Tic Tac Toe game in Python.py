# Tic Tac Toe game in Python

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Rows, columns and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    return [player, player, player] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for turn in range(9):
        print_board(board)
        print(f"Player {player}, choose your position (row and column):")

        while True:
            try:
                row = int(input("Row (0,1,2): "))
                col = int(input("Column (0,1,2): "))
                if board[row][col] == " ":
                    break
                else:
                    print("Position already taken. Try again.")
            except:
                print("Invalid input! Enter numbers between 0 and 2.")

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")

tic_tac_toe()
