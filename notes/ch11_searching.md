# Searching

## Binary Search

```python
def bsearch(t, A):
  L, U = 0, len(A) - 1
  while L <= U:
    M = L + (U - L) // 2 ## To avoid overflow
    if A[M] == t:
      return M
    elif A[M] < t:
      L = M + 1
    else:
      U = M - 1
  return -1
```

- Use `bisect` library

  ```python
  >>> import bisect
  >>> l = [1, 3, 4, 4, 4, 6, 7]
  
  >>> bisect.bisect_left(l, 4) # First entry that is >= targeted value
  2
    
  >>> bisect.bisect_right(l, 4) # First entry that is > targeted value
  5
  ```

  - If target > everything in the list, `len(l)` is returned, so need to check that


## Partition

- To partition an array at a given pivot index

  ```python
  def partition_around_pivot(left, right, pivot_idx):
    """
    Partitions A[left:right + 1] around pivot_idx so that
    Elements > pivot are on the left, <= pivot are on the right.
    Returns the new index of the pivot, pivot_idx_new, after partitioning.
    """
    pivot_val = A[pivot_idx]
    # Placeholder for where to insert the large numbers next
    pivot_idx_new = left
    # Swap pivot and the last element so it doesn't get in the way
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    
    # Iterate through all numbers (pivot, now at the last position, is not included)
    for i in range(left, right):
      # Large number
      if A[i] > pivot_val:
        # Swap with the placeholder
        A[i], A[pivot_idx_new] = A[pivot_idx_new], A[i]
        # Increment placeholder
        pivot_idx_new += 1
        
    # Swap placeholder (must be smaller) with pivot, so the structure is restored
    A[pivot_idx_new], A[right] = A[right], A[pivot_idx_new]
    # Return new index position
    return pivot_idx_new
  ```

  

