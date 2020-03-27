import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# # Returns the number of valid entries after deletion.
# def delete_duplicates(A: List[int]) -> int:
#     n = len(A)
#     # Corner cases
#     if n <= 1:
#         return n
#
#     # Make all duplicates "d", in-place
#     prev_val = A[0]
#     num_duplicates = 0
#     for i in range(1, len(A)):
#         # Duplicate detected
#         if A[i] == prev_val:
#             num_duplicates += 1
#             A[i] = "d"
#         # Not a duplicate
#         else:
#             prev_val = A[i]
#
#     # No duplicates
#     if num_duplicates == 0:
#         return n
#     # Yes duplicates
#     else:
#         # Shift all non-duplicates to the left
#         idx = 0
#         for i in range(0, len(A)):
#             if A[i] != "d":
#                 A[idx] = A[i]
#                 idx += 1
#         # Make last num_duplicates digits 0
#         A[-num_duplicates:] = [0] * num_duplicates
#         return n - num_duplicates


def delete_duplicates(A: List[int]) -> int:
    # Corner cases
    n = len(A)
    if n <= 1:
        return n

    prev_val = A[0]
    idx = 1
    for i in range(1, len(A)):
        if A[i] != prev_val:
            A[idx] = A[i]
            prev_val = A[i]
            idx += 1

    return idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
