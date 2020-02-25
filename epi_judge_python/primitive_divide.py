from test_framework import generic_test


def divide(x: int, y: int) -> int:
    result, power = 0, 32
    y_power = y << power

    while x >= y:
        # Try to find the largest k such that 2^k y <= x
        while y_power > x:
            y_power >>= 1
            power -= 1

        # Add 2^k to the quotient
        result += 1 << power

        # Decrease x by 2^k y
        x -= y_power

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
