from test_framework import generic_test


def swap_bits(x, i, j):
    # Extract ith and jth bits
    x_i = (x >> i) & 1
    x_j = (x >> j) & 1

    # Swap if different
    if x_i != x_j:
        bit_mask = (1 << i) | (1 << j)  # Bits at ith and jth positions are both 1
        x ^= bit_mask  # Set to complement, since x_i != x_j this is essentially swapping
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
