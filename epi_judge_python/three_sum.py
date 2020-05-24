from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    def has_two_sum(k: int) -> bool:
        for n in A:
            if k - n in A:
                return True
        return False

    return any(has_two_sum(t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
