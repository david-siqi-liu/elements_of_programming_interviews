from test_framework import generic_test


# def reverse(x: int) -> int:
#     # If x is 0
#     if x == 0:
#         return 0
#     # If x is negative, reverse its absolute value and add negative sign in front
#     elif x < 0:
#         return -1 * reverse(abs(x))
#     # x is positive
#     else:
#         return int(str(x)[::-1])

def reverse(x: int) -> int:
    # Iteratively mod 10
    result = 0
    x_remaining = abs(x)

    # Suppose input = -1132
    # result initializes to 0, x_remaining initializes to 1132
    # result increments by 1132 % 10 = 2, which is the most significant digit of x_remaining
    # Now, result is 2, x_remaining is 113
    # Next, result becomes 2 * 10 + 3 = 23, x_remaining becomes 11
    # Then 231 and 1
    # Then 2311 and 0 (since 1 // 10 = 0)
    while x_remaining > 0:
        result = result * 10 + x_remaining % 10
        x_remaining = x_remaining // 10

    if x < 0:
        return -1 * result
    else:
        return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
