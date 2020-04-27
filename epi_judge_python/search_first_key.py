from typing import List

from test_framework import generic_test


# import bisect
# def search_first_of_k(A: List[int], k: int) -> int:
#     if len(A) == 0:
#         return -1
#
#     result = bisect.bisect_left(A, k)
#     if result == len(A) or A[result] != k:
#         return -1
#     else:
#         return result

def search_first_of_k(A: List[int], k: int) -> int:
    lower, upper = 0, len(A) - 1
    result = -1
    while lower <= upper:
        middle = lower + (upper - lower) // 2
        if A[middle] == k:
            result = middle
            upper = middle - 1
        elif A[middle] < k:
            lower = middle + 1
        else:
            upper = middle - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
