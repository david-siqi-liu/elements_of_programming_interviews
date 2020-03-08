# Linked List

- Singly - has a reference to the next node
- Doubly - also has a reference to the previous/predecessor node, in which case a self-loop can be used (instead of NULL) to mark the end of the list
- Key differences with list
  - Inserting/deleting from LL is cheap - O(1)
  - Accessing a particular (kth) element from LL is expensive - O(k)

- Basic LL implementation

  ```python
  class ListNode:
    def __init__(self, data=0, next_node=None):
      self.data = data
      self.next = next_node
     
    def __eq__(self, other):
      a, b = self, other
      while a and b:
        if a.data != b.data:
          return False
        a, b = a.next, b.next
      return a is None and b is None
  ```

- Searching

  ```python
  # Recursive
  def search_list(L, key):
    if L and L.data == key:
      return L
    elif L:
      return search_list(L.next)
    else:
      return None
  
  # Iterative
  def search_list(L, key):
    while L and L.data != key:
      L = L.next
    return L
  ```

- Inserting after a node

  ```python
  def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node
  ```

- Deleting after a node

  ```python
  def delete_after(node):
    if node.next:
      node.next = node.next.next
    else:
      node.next = None
  ```

- If the required return is a LL, can

  - Create a dummy head using ListNode()
  - Return dummy head.next
  - DO NOT initialize to None!

- To reverse a singly LL iteratively

  ```python
  def reverse_list(head):
    ptr_prev = None
    ptr_curr = head
    ptr_next = None
    while ptr_curr:
      ptr_next = ptr_curr.next # Stash the next node
      ptr_curr.next = ptr_prev # Reverse!
      ptr_prev = ptr_curr # Prepare for next iteration
      ptr_curr = ptr_next
    return prev
  ```

- To detect cycle

  ```python
  def has_cycle(head):
      # Floyd's Tortoise and Hare algorithm
      tortoise = hare = head
      while hare and hare.next:
          tortoise = tortoise.next
          hare = hare.next.next
          if tortoise is hare: # Equality is defined in ListNode class
              return tortoise
      return None
  ```

  