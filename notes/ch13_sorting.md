# Sorting

- Recap

  - `.sort()` sorts in-place. Can specify a `key` using lambda function for entries in the array

  - `sorted` returns a new instance. Also takes in `key`

    ```python
    # Reorder the logs so that all of the letter-logs come before any digit-log
    # The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties
    # The digit-logs should be put in their original order
    def order(log: str):
        identifier, others = log.split(" ", 1)
        if identifier[0] == 'l':
            return (0, others, identifier)
        else:
            return (1,)
                
    sorted(logs, key=order) 
    ```

    

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
