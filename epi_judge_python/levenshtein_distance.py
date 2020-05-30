from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # M[b][a] denotes the edit distance from A[0:a] to B[0:b]
    M = [[0 for a in range(len(A) + 1)] for b in range(len(B) + 1)]
    for a in range(1, len(A) + 1):
        M[0][a] = a
    for b in range(1, len(B) + 1):
        M[b][0] = b

    for b in range(1, len(B) + 1):
        for a in range(1, len(A) + 1):
            if A[a - 1] == B[b - 1]:
                M[b][a] = M[b - 1][a - 1]
            else:
                M[b][a] = 1 + min(M[b - 1][a - 1],  # Sub
                                  M[b - 1][a],  # Insert
                                  M[b][a - 1])  # Delete

    return M[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
