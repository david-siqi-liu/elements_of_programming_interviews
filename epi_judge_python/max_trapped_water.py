from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water, (right - left) * min(heights[left], heights[right]))
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return max_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
