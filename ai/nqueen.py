def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    # Check this row on the left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solveNqueen(board, col, n):
    if col >= n:
        print_board(board)
        return True

    res = False
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solveNqueen(board, col + 1, n) or res
            board[row][col] = 0  # backtrack
    return res

def Nqueen(n):
    board = [[0] * n for _ in range(n)]
    if not solveNqueen(board, 0, n):
        print("No Solution")

# Call the main function here
if __name__ == "__main__":
    Nqueen(4)  # You can change 4 to any N to test N-Queens
