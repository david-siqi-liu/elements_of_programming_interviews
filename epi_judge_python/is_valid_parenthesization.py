from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    brackets = []
    lookup = {'(': ')', '[': ']', '{': '}'}

    for b in s:
        if b in lookup.keys():
            brackets.append(b)
        else:
            if len(brackets) == 0 or lookup[brackets.pop()] != b:
                return False

    return len(brackets) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
