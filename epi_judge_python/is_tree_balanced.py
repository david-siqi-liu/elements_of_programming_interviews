import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def get_height(tree):
    if not tree:
        return 0

    return max(get_height(tree.left), get_height(tree.right)) + 1


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    if not is_balanced_binary_tree(tree.left) or not is_balanced_binary_tree(tree.right):
        return False

    return abs(get_height(tree.left) - get_height(tree.right)) <= 1


# def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
#     BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight',
#                                                       ('balanced', 'height'))
#
#     def check_balanced(tree):
#         if not tree:
#             return BalancedStatusWithHeight(True, -1)
#
#         left_result = check_balanced(tree.left)
#         right_result = check_balanced(tree.right)
#         if not left_result.balanced or not right_result.balanced:
#             return BalancedStatusWithHeight(False, 0)
#
#         is_balanced = abs(left_result.height - right_result.height) <= 1
#         height = max(left_result.height, right_result.height) + 1
#         return BalancedStatusWithHeight(is_balanced, height)
#
#     return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
