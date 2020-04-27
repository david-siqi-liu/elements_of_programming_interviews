import math
from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition_around_pivot(left, right, pivot_idx):
        """
        Partitions A[left:right + 1] around pivot_idx so that elements > pivot are on the left, <= pivot are on the right.
        Returns the new index of the pivot, pivot_idx_new, after partitioning.
        """
        pivot_val = A[pivot_idx]
        # Placeholder for where to insert the large numbers next
        pivot_idx_new = left
        # Swap pivot and the last element so it doesn't get in the way
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        # Iterate through all numbers (pivot, now at the last position, is not included)
        for i in range(left, right):
            # Large number
            if A[i] > pivot_val:
                # Swap with the placeholder
                A[i], A[pivot_idx_new] = A[pivot_idx_new], A[i]
                # Increment placeholder
                pivot_idx_new += 1
        # Swap placeholder (must be smaller) with pivot, so the structure is restored
        A[pivot_idx_new], A[right] = A[right], A[pivot_idx_new]
        # Return new index position
        return pivot_idx_new

    left, right = 0, len(A) - 1
    while left <= right:
        # Pivot in the middle
        pivot_idx = math.floor((left + right) / 2)
        # New index of the same pivot after partitioning
        pivot_idx_new = partition_around_pivot(left, right, pivot_idx)
        # If there are exactly k - 1 elements to the left of the pivot, kth largest must be the pivot
        if pivot_idx_new == k - 1:
            return A[pivot_idx_new]
        # If there are more than k - 1 elements to the left of the pivot, kth largest must be in the left
        elif pivot_idx_new > k - 1:
            right = pivot_idx_new - 1
        # If there are left than k - 1 elements to the left of the pivot, kth largest must be in the right
        else:
            left = pivot_idx_new + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
