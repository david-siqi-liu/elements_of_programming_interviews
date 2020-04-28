from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    idx_A, idx_B = m - 1, n - 1
    idx_write = m + n - 1

    while idx_A >= 0 and idx_B >= 0:
        if A[idx_A] >= B[idx_B]:
            A[idx_write] = A[idx_A]
            idx_A -= 1
        else:
            A[idx_write] = B[idx_B]
            idx_B -= 1
        idx_write -= 1

    if idx_B >= 0:
        A[:idx_write + 1] = B[:idx_B + 1]

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
