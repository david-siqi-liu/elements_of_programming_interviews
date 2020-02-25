from test_framework import generic_test


def power(x: float, y: int) -> float:
    # Base cases
    if y == 0:
        return 1.0
    elif y == 1:
        return x

    # If y is negative, x^y = (1/x)^(-y)
    if y < 0:
        return power(1.0 / x, -y)

    # If y is even x^y = (x^(y/2))^2
    if y & 1 == 0:
        return power(x, (y >> 1)) ** 2
    # If y is odd, x^y = x * (x^(y/2))^2
    else:
        return x * power(x, (y >> 1)) ** 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
