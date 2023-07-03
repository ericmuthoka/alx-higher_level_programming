import sys

def is_safe(board, row, col):
    # Check if it is safe to place a queen at board[row][col]
    # in the current board configuration

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    # Solve the N-Queens problem using backtracking

    if row == N:
        # All queens are placed, print the solution
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
        print()
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0

if __name__ == '__main__':
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0] * N for _ in range(N)]

    # Solve the N-Queens problem
    solve_nqueens(board, 0)
