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

  - Enqueue & dequeue

    ```python
    # List implementation
    >>> s = []
    
    # Enqueue
    >>> s.append('a')
    
    # Peek
    >>> s[0]
    'a'
    
    # Dequeue
    >>> s.pop(0)
    'a'
    >>> s
    []
    
    # Size
    >>> len(s)
    0
    
    # IndexError for both Enqueue and Dequeue on an empty Queue
    >>> s[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
    
    >>> s.pop(0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: pop from empty list
    ```

- Priority Queue (min-heap)

  ```python
  import heapq
  
  customers = []
  
  heapq.heappush(customers, (2, "Harry"))
  heapq.heappush(customers, (3, "Charles"))
  heapq.heappush(customers, (1, "Riya"))
  heapq.heappush(customers, (4, "Stacy"))
  
  while customers:
       print(heapq.heappop(q))
          
  # Riya, Harry, Charles, Stacy.
  ```

  - Need to implement `__lt__` if want to use custom class