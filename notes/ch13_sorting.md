# Sorting

- Recap

  - `.sort()` sorts in-place. Can specify a `key` using lambda function for entries in the array
  - `sorted` returns a new instance. Also takes in `key`

- For custom class, need to implement `__eq__`, `__lt__` functions

- To remove duplicates from an array in-place

  ```python
  def eliminate_duplicate(A):
  	A.sort()
  	write_idx = 1
  	for cand in A[1:]:
  		if cand != A[write_idx - 1]:
  			A[write_idx] = cand
  			write_idx += 1
    del A[write_idx:]
  ```

