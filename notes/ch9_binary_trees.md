# Binary Trees

- Traversals

  ```python
  def tree_traversal(root):
    if root:
      # Pre-order: root, left, right
      # In-order: left, root, right
      # Post-order: left, right, root
      print('Preorder: %d' % root.data)
      tree_traversal(root.left)
      print('Inorder: %d' % root.data)
      tree_traversal(root.right)
      print('Postorder: %d' % root.data)
  ```

  - Time: O(n)
  - Space: O(h), minimum of h is log(n) and maximum of h is n

