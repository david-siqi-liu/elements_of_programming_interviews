from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_mirror_image(t1: BinaryTreeNode, t2: BinaryTreeNode) -> bool:
    if not t1 and not t2:
        return True
    elif not t1 and t2:
        return False
    elif t1 and not t2:
        return False
    else:
        return t1.data == t2.data and is_mirror_image(t1.left, t2.right) and is_mirror_image(t1.right, t2.left)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    return is_mirror_image(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
