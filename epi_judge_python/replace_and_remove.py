import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # Forward pass - remove 'b' and count number of 'a'
    write_index = 0
    num_a = 0
    for i in range(size):
        # This includes 'a' as well
        if s[i] != "b":
            s[write_index] = s[i]
            write_index += 1
        if s[i] == "a":
            num_a += 1

    # Backward pass - replace 'a' with 'dd'
    curr_index = write_index - 1
    write_index = write_index + num_a - 1
    final_size = write_index + 1
    while curr_index >= 0:
        if s[curr_index] == "a":
            s[write_index - 1: write_index + 1] = ["d", "d"]
            write_index -= 2
        else:
            s[write_index] = s[curr_index]
            write_index -= 1
        curr_index -= 1

    return final_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
