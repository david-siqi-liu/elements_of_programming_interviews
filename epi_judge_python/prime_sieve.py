from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    A = list(range(2, n + 1))

    primes = []
    for i in range(0, len(A)):
        a = A[i]
        if a != 0:
            primes.append(a)
            A[i::a] = [0] * len(A[i::a])

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
