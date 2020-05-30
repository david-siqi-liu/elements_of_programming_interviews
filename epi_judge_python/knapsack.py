import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    # M[i][w] denotes the max value for items[0:i] subject to weight w
    M = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(len(items)):
        for w in range(capacity):
            if items[i].weight <= w + 1:
                M[i + 1][w + 1] = max(M[i][w + 1],
                                      items[i].value + M[i][w + 1 - items[i].weight])
            else:
                M[i + 1][w + 1] = M[i][w + 1]

    return M[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
