from typing import List

from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    m, n = len(grid), len(grid[0])
    M = [[0 for _ in range(n)] for _ in range(m)]

    for p in range(len(pattern)):
        for y in range(m):
            for x in range(n):
                if grid[y][x] == pattern[p]:
                    if p == 0:
                        M[y][x] = 1
                    else:
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0 <= x + dx < n and 0 <= y + dy < m and \
                                    M[y + dy][x + dx] == p:
                                M[y][x] = p + 1
                                break
    for y in range(m):
        for x in range(n):
            if M[y][x] == len(pattern):
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
