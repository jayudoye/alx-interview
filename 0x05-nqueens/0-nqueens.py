#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
"""
import sys


def is_safe(board: list, row: int, col: int, N: int) -> bool:
    """
    Check if placing a queen at position (row, col) is safe.

    Args:
    board (list): The current state of the chessboard.
    row (int): The row index of the position to check.
    col (int): The column index of the position to check.
    N (int): The size of the chessboard.

    Returns:
    bool: True if it is safe to place a queen at position (row, col), False
    otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board: list, row: int, N: int, solutions: list) -> None:
    """
    Recursively solve the N queens problem.

    Args:
    board (list): The current state of the chessboard.
    row (int): The current row being considered.
    N (int): The size of the chessboard.
    solutions (list): List to store the solutions.

    Returns:
    None
    """
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0


def nqueens(N: str) -> None:
    """
    Solve the N queens problem.

    Args:
    N (str): The size of the chessboard.

    Returns:
    None
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
