import collections
from typing import List

from test_framework import generic_test

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    s = Coordinate(x, y)
    color = image[x][y]
    status = collections.defaultdict(lambda: 'undiscovered')
    status[s] = 'discovered'
    queue = [s]
    while queue:
        v = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            w = Coordinate(v.x + dx, v.y + dy)
            if status[w] == 'undiscovered' \
                    and 0 <= w.x < len(image) \
                    and 0 <= w.y < len(image[w.x]) \
                    and image[w.x][w.y] == color:
                status[w] = 'discovered'
                queue.append(w)
        status[v] = 'visited'

    for c, v in status.items():
        if v != 'undiscovered':
            image[c.x][c.y] = 1 - color

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
