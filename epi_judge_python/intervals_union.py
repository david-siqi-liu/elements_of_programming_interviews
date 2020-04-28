import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []

    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))

    unions = [intervals[0]]
    for i in intervals[1:]:
        # If the following
        #   1. New interval's left endpoint is less than current interval's right endpoint
        #   2. Same, but one of them is closed
        if (i.left.val < unions[-1].right.val) or (
                i.left.val == unions[-1].right.val and (i.left.is_closed or unions[-1].right.is_closed)):
            # Update if
            #   1. New interval's right endpoint if further than current interval's right endpoint
            #   2. Same, but new interval's right endpoint is closed
            if (i.right.val > unions[-1].right.val) or (
                    i.right.val == unions[-1].right.val and i.right.is_closed):
                unions[-1] = Interval(unions[-1].left, i.right)
        # All other cases, non-overlapping
        else:
            unions.append(i)

    return unions


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
