import collections
from typing import List

from test_framework import generic_test

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def fill_surrounded_regions(board: List[List[str]]) -> None:
    m, n = len(board), len(board[0])
    status = collections.defaultdict(lambda: 'undiscovered')
    queue = []
    # Top and bottom
    for x in range(n):
        if board[0][x] == 'W':
            queue.append(Coordinate(x, 0))
            status[Coordinate(x, 0)] = 'discovered'
        if board[m - 1][x] == 'W':
            queue.append(Coordinate(x, m - 1))
            status[Coordinate(x, m - 1)] = 'discovered'
    # Left and right
    for y in range(1, m - 1):
        if board[y][0] == 'W':
            queue.append(Coordinate(0, y))
            status[Coordinate(0, y)] = 'discovered'
        if board[y][n - 1] == 'W':
            queue.append(Coordinate(n - 1, y))
            status[Coordinate(n - 1, y)] = 'discovered'
    # BFS
    while queue:
        v = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            w = Coordinate(v.x + dx, v.y + dy)
            if status[w] == 'undiscovered' and \
                    0 <= w.x < n and \
                    0 <= w.y < m and \
                    board[w.y][w.x] == 'W':
                queue.append(w)
        status[v] = 'visited'
    # Turn all non-visited
    for y in range(m):
        for x in range(n):
            if board[y][x] == 'W' and status[Coordinate(x, y)] == 'undiscovered':
                board[y][x] = 'B'
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
