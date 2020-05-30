from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # Subproblems: find the maximum of the subarray INCLUDING A[k]
    n = len(A)
    maxes = [0 for _ in range(n + 1)]
    for i in range(n):
        maxes[i + 1] = max(maxes[i], 0) + A[i]
    return max(maxes)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
