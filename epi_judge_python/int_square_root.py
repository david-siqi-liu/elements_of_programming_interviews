from test_framework import generic_test


def square_root(k: int) -> int:
    left, right = 0, k
    while left <= right:
        middle = left + (right - left) // 2
        middle_squared = middle ** 2
        if middle_squared == k:
            return middle
        elif middle_squared < k:
            left = middle + 1
        else:
            right = middle - 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
