from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    if not A:
        return [[]]

    results: List[List[int]] = []

    for i in range(0, len(A)):
        if i == 0:
            others = permutations(A[1:])
        elif i < len(A) - 1:
            others = permutations(A[:i] + A[i + 1:])
        else:
            others = permutations(A[:-1])

        for j in others:
            results.append([A[i]] + j)

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
