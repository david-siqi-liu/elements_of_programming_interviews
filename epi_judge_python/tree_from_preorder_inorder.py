from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    if len(preorder) == 0:
        return None

    root_data = preorder[0]
    root_node = BinaryTreeNode(root_data)
    root_pos_inorder = inorder.index(root_data)

    # No left sub-tree
    if root_pos_inorder == 0:
        left_inorder = []
        right_inorder = inorder[1:]
        left_preorder = []
        right_preorder = preorder[1:]
    # No right sub-tree
    elif root_pos_inorder == len(inorder) - 1:
        left_inorder = inorder[:-1]
        right_inorder = []
        left_preorder = preorder[1:]
        right_preorder = []
    # Both left and right
    else:
        left_inorder = inorder[:root_pos_inorder]
        right_inorder = inorder[root_pos_inorder + 1:]
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

    root_node.left = binary_tree_from_preorder_inorder(left_preorder,
                                                       left_inorder)
    root_node.right = binary_tree_from_preorder_inorder(right_preorder,
                                                        right_inorder)

    return root_node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
