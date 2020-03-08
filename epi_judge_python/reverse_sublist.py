from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = sublist_prev = ListNode()
    sublist_prev.next = L

    # sublist_prev points to the node right before the starting node
    for _ in range(start - 1):
        sublist_prev = sublist_prev.next

    # Starting node might be the last one, in which case we just return the original
    # Otherwise, we need to reverse the sublist
    if sublist_prev and sublist_prev.next:
        sublist_head = sublist_prev.next
    else:
        return L

    # Reverses sublist
    ptr_prev = None
    ptr_curr = sublist_head
    ptr_next = None
    for _ in range(finish - start + 1):
        ptr_next = ptr_curr.next  # Stash the next node
        ptr_curr.next = ptr_prev  # Reverse!
        ptr_prev = ptr_curr  # Make the current node the new previous node
        ptr_curr = ptr_next  # Make the next node the current node (to be examined next)

    # Set pointer for prev -> finish
    sublist_prev.next = ptr_prev
    # Set pointer for start -> later
    sublist_head.next = ptr_curr

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
