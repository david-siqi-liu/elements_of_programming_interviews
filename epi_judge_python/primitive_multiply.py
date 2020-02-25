from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    a = min(x, y)
    b = max(x, y)
    product = 0
    n = 0

    # Get the length of a's binary representation
    for i in range(64):
        if (a >> i) & 1 == 1:
            n = i

    # Iterate through a's binary representation
    for i in range(n + 1):
        # ith element of a
        a_i = (a >> i) & 1
        # If a_i is 1, then shift b by i and add to product
        if a_i == 1:
            product += (b << i)

    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
