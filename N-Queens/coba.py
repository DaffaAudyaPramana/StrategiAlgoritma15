def is_valid(board, row, col, n):
    # Check if the current queen placement is valid
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - row + i >= 0 and board[i][col - row + i] == 1:
            return False
        if col + row - i < n and board[i][col + row - i] == 1:
            return False
    return True

def solve_n_queens(board, row, n):
    # Base case: all queens have been placed
    if row == n:
        return True

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0

    # If no valid placement is found, backtrack to the previous row
    return False

def n_queens(n):
    # Initialize the board with zeros
    board = [[0] * n for i in range(n)]
    # Call the solve_n_queens function starting from the first row
    solve_n_queens(board, 0, n)
    # Print the solution if one is found
    if solve_n_queens(board, 0, n):
        for i in range(n):
            print(board[i])
    else:
        print("No solution found")
