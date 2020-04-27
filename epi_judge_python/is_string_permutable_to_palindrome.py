import collections

from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    """
    If and only if the number of chars whose frequencies is odd is at most 1
    """
    c = collections.Counter(s)
    num_odds = 0
    for k, v in c.items():
        if v % 2 == 1:
            num_odds += 1
            if num_odds > 1:
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
