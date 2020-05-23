import collections
import itertools
from typing import Set

from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    if len(s) != len(t):
        return -1

    def off_by_one(s1: str, s2: str) -> bool:
        if s1 == s2:
            return False
        if len(s1) != len(s2):
            return False
        off = False
        for i, c1 in enumerate(s1):
            c2 = s2[i]
            if c1 != c2:
                if off:
                    return False
                else:
                    off = True
        return True

    # Build graph of one-off strings
    graph = collections.defaultdict(set)
    for s1, s2 in itertools.combinations(D, 2):
        if off_by_one(s1, s2):
            graph[s1].add(s2)
            graph[s2].add(s1)

    # BFS
    status = collections.defaultdict(lambda: 'undiscovered')
    status[s] = 'discovered'
    dist = collections.defaultdict(lambda: -1)
    dist[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if status[w] == 'undiscovered':
                status[w] = 'discovered'
                dist[w] = dist[v] + 1
                queue.append(w)
            if w == t:
                return dist[w]
        status[v] = 'visited'

    # Return
    return dist[t]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
