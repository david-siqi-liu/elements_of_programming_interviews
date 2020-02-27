import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    # To aim for O(1) space usage
    # Pointers for end of even/beginning of odd
    even, odd = 0, len(A) - 1

    # Even pointer is before odd pointer
    while even < odd:
        # Element at even pointer is indeed even
        if A[even] % 2 == 0:
            even += 1
        # Element at even pointer is actually odd, swap
        else:
            A[even], A[odd] = A[odd], A[even]
            odd -= 1

    return A


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
