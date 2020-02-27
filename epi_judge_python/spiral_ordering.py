from typing import List

from test_framework import generic_test

import math


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)
    result = []

    # If n = 3, offset = {0}
    # If n = 4, offset = {0, 1}
    # If n = 5, offset = {0, 1}, ...
    for offset in range(0, math.ceil(n / 2)):
        # Top border, all values (except for the last value)
        result.extend(square_matrix[offset][offset:n - offset - 1])
        # Right border, last value in all rows (except for the last row)
        result.extend([square_matrix[i][-1 - offset] for i in range(offset, n - offset - 1)])
        # Bottom border, all values in last row (except for the first value), reversed!
        result.extend(square_matrix[-1 - offset][offset + 1:n - offset][::-1])
        # Left border, first value in all rows (except for the first row), reversed!
        result.extend([square_matrix[i][offset] for i in reversed(range(offset + 1, n - offset))])

    # If n is odd, add center piece
    if n % 2 == 1:
        result.append(square_matrix[n // 2][n // 2])

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
