# Stacks and Queues

- Can be implemented using LL or List

- Stacks - LIFO

  - Push & pop (both O(1))

  - Peek (O(1))

    ```python
    # List implementation
    >>> s = []
    
    # Push
    >>> s.append('a')
    
    # Peek
    >>> s[-1]
    'a'
    
    # Pop
    >>> s.pop()
    'a'
    >>> s
    []
    
    # Size
    >>> len(s)
    0
    
    # IndexError for both Peek and Pop on an empty Stack
    >>> s[-1]
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    IndexError: list index out of range
      
    >>> s.pop()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    IndexError: pop from empty list
    ```

- Queues - FIFO

- 