import collections
from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # Keep all buildings that potentially have a view in a stack
    # Given a new building (west of all existing buildings), compare it with the top of the stack
    # If the new building is taller than the top of the stack building, then pop the top of the stack building
    # Do this until the top of the stack is taller, then push the new building onto the stack
    # Essentially, the stack is in an increasing order of height, from West to East
    # Finally, return the stack in reversed order (i.e., starting from the East (tallest))

    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('idx', 'height'))

    candidates = []

    for idx, height in enumerate(sequence):
        while candidates and height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(idx, height))

    return [c.idx for c in reversed(candidates)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
