from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalnum() and s[j].isalnum():
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        elif not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            i += 1
            j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
