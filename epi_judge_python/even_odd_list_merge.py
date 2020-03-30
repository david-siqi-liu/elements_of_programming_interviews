from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# def even_odd_merge(L: ListNode) -> Optional[ListNode]:
#     if not L:
#         return ListNode().next
#     elif not L.next:
#         return L
#
#     evens, odds = L, L.next
#     evens_head, odds_head = evens, odds
#     curr_num = 2
#     while True:
#         if curr_num % 2 == 0:
#             if odds.next:
#                 evens.next = odds.next
#                 evens = evens.next
#             else:
#                 evens.next = None
#                 break
#         else:
#             if evens.next:
#                 odds.next = evens.next
#                 odds = odds.next
#             else:
#                 odds.next = None
#                 break
#         curr_num += 1
#
#     evens.next = odds_head
#
#     return evens_head

def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    evens_head, odds_head = ListNode(0), ListNode(0)
    tails = [evens_head, odds_head]
    turn = 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[1].next = None
    tails[0].next = odds_head.next

    return evens_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
