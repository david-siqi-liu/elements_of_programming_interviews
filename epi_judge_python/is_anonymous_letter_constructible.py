import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    counter_letter = collections.Counter(letter_text)
    counter_magazine = collections.Counter(magazine_text)

    return len(counter_letter - counter_magazine) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
