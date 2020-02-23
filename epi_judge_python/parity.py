from test_framework import generic_test


def parity(x: int) -> int:
    result = 0
    while x:
        # if last digit (binary representation) is 1
        if x & 1:
            result ^= 1  # 1 becomes 0, 0 becomes 1
        x >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
