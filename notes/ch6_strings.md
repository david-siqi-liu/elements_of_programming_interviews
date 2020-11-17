# Strings

- Traversal

  ```python
  >>> s = "abcde"
  
  # Normal
  >>> [s[i] for i in range(len(s))]
  ['a', 'b', 'c', 'd', 'e']
  
  # Reverse, but start from first one still
  >>> [s[-i] for i in range(len(s))]
  ['a', 'e', 'd', 'c', 'b']
  
  # Reverse completely
  >>> [s[~i] for i in range(len(s))]
  ['e', 'd', 'c', 'b', 'a']
  
  # Or can do
  >>> [c for c in reversed(s)]
  ```

- Other

  ```python
  # Check alphanumerical
  >>> "a".isalnum()
  True
  >>> ",".isalnum()
  False
  
  ```
# Remove punctuations
```
paragraph = re.sub(r'[\!\?\'\,\;\.]', ' ', paragraph) # Replace with space, not empty
```

  

