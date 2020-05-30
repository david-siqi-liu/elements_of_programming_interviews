from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    num_scores = len(individual_play_scores)

    # M[i][j] = number of combinations to achieve j using the first i score types
    M = [[0 for j in range(final_score + 1)] for i in range(num_scores + 1)]
    for i in range(num_scores + 1):
        M[i][0] = 1

    # Fill out the matrix row-by-row (i.e., score type by score type)
    for i in range(1, num_scores + 1):
        for j in range(1, final_score + 1):
            M[i][j] = M[i - 1][j]
            if j >= individual_play_scores[i - 1]:
                M[i][j] += M[i][j - individual_play_scores[i - 1]]

    return M[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
