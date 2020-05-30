from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    M = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        M[0][i] = 1
    for j in range(m):
        M[j][0] = 1

    for j in range(1, m):
        for i in range(1, n):
            M[j][i] = M[j - 1][i] + M[j][i - 1]

    return M[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
