from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # Check rows
    if any(
            not is_valid_sudoku_subarray([partial_assignment[r][c] for c in range(9)])
            for r in range(9)):
        return False

    # Check columns
    if any(
            not is_valid_sudoku_subarray([partial_assignment[r][c] for r in range(9)])
            for c in range(9)):
        return False

    # Check 3x3 2D subarray
    if any(
            not is_valid_sudoku_subarray([partial_assignment[R * 3 + r][C * 3 + c] for r in range(3) for c in range(3)])
            for R in range(3) for C in range(3)):
        return False

    return True


# Helper function to check if there's no duplicate in a given list of integers (except for 0)
def is_valid_sudoku_subarray(A: List[int]) -> bool:
    A = list(filter(lambda x: x != 0, A))
    return len(A) == len(set(A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
