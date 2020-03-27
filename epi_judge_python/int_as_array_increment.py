from typing import List

from test_framework import generic_test


# def plus_one(A: List[int]) -> List[int]:
#     idx = len(A) - 1
#     result = []
#     while True:
#         if A[idx] < 9:
#             result = A[:idx] + [A[idx] + 1] + result
#             break
#         elif idx == 0:
#             result = [1, 0] + result
#             break
#         else:
#             idx -= 1
#             result = [0] + result
#     return result

def plus_one(A: List[int]) -> List[int]:
    # Increment the last digit by 1
    A[-1] += 1
    # Iterate through the array in reversed order
    for i in reversed(range(1, len(A))):
        # Not a carry-out, done iterating
        if A[i] < 10:
            break
        # Carry-out
        else:
            # Set current digit to 0
            A[i] = 0
            # Increment previous digit
            A[i - 1] += 1
    # Check if first digit is 10
    if A[0] == 10:
        A[0] = 0
        A.insert(0, 1)
    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
