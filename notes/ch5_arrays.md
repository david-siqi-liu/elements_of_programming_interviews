# Arrays

- To initiate a list

  ```python
  >>> [3, 5, 6, 7]
  [3, 5, 6, 7]
  
  >>> [1] + [0] * 3
  [1, 0, 0, 0]
  
  >>> list(range(5))
  [0, 1, 2, 3, 4]
  ```

- Basic operations

  ```python
  # All in-place
  
  >>> a = [3, 5, 6, 7]
  >>> a.insert(3, 8) # Positional
  >>> a
  [3, 5, 6, 8, 7]
  
  >>> a.append(9) # Always at the end
  >>> a
  [3, 5, 6, 8, 7, 9]
  
  >>> a.remove(2) # ValueError if not exist
  Traceback (most recent call last):
    File "<input>", line 1, in <module>
  ValueError: list.remove(x): x not in list
      
  >>> a.remove(3) # Removes first occurrence
  >>> a
  [5, 6, 8, 7, 9]
  
  >>> l = [1, 3] # Extend
  >>> l.extend([2, 4])
  >>> l
  [1, 3, 2, 4]
  >>> l.extend([[5, 6]])
  >>> l
  [1, 3, 2, 4, [5, 6]]
  ```

- Copy

  ```python
  # Shallow, changing a also changes b
  >>> b = a
  
  # Deep, changing a does not affect c
  >>> c = list(a)
  
  # Deep
  >>> c = a[:]
  ```

- Methods

  ```python
  >>> a = [1, 2, 3]
  >>> a.reverse() # In-place
  >>> a
  [3, 2, 1]
  
  >>> reversed(a) # Iterator
  <list_reverseiterator object at 0x10e144dd0>
  
  >>> b = [5, 4, 6]
  >>> b.sort() # In-place
  >>> b
  [4, 5, 6]
  
  >>> b = [5, 4, 6] 
  >>> sorted(b) # Returns a copy, original is unchanged
  [4, 5, 6]
  ```

- Delete

  ```python
  >>> b = [5, 4, 6] 
  >>> del b[1] # Just one
  >>> b
  [5, 6]
  
  >>> a = [1, 2, 3, 4, 5]
  >>> del a[1:4] # Delete the entire slice (1, 2 and 3)
  >>> a
  [1, 5]
  ```

- List comprehensions

  ```python
  >>> A = [1, 3, 5]
  >>> B = ['a', 'b']
  >>> [(x, y) for x in A for y in B]
  [(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]
  
  >>> A = [[1, 2, 3], [4, 5, 6]]
  >>> [[x ** 2 for x in row] for row in A]
  [[1, 4, 9], [16, 25, 36]]
  ```
