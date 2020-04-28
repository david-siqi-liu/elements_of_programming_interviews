from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    if len(input_set) == 0:
        return [[]]
    elif len(input_set) == 1:
        return [[], [input_set[0]]]
    else:
        others = generate_power_set(input_set[1:])
        return [[input_set[0]] + o for o in others] + others


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
