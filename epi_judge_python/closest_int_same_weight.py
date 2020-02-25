from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    # Idea: swap the two rightmost consecutive bits that differ (i.e., 01 or 10)
    for i in range(63):
        j = i + 1
        x_i = (x >> i) & 1
        x_j = (x >> j) & 1

        # If ith element and (i + 1)th element are different
        if x_i != x_j:
            bit_mask = (1 << i) | (1 << j)  # Bits at ith and (i + 1)th positions are both 1
            x ^= bit_mask  # Set to complement, since x_i != x_j this is essentially swapping
            break

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
