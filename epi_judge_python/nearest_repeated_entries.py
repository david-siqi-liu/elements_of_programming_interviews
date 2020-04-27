import collections
from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_index = collections.defaultdict(int)
    closest = float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            closest = min(closest,
                          i - word_to_latest_index[word])
        word_to_latest_index[word] = i
    if closest == float('inf'):
        return -1
    else:
        return closest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
