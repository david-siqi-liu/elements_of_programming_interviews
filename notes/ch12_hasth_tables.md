# Hash Tables

- O(1) time for inserts, deletes and lookups

- Needs good hash function (rarely an issue in practice)

- Mutliple data structures can be used for hash table - none allows for duplicate keys, unlike `list`

  |                           | Stores                | Value Look-Up |
  | ------------------------- | --------------------- | ------------- |
  | `set`                     | Keys                  | N/A           |
  | `dict`                    | Key-Value Pairs       | `KeyError`    |
  | `collections.defaultdict` | Key-Value Pairs       | Default value |
  | `collections.Counter`     | Key-Value Pairs (Int) | 0             |

- `set`

  - `add`, `remove` (`KeyError` if not present), `discard` (no `KeyError`)
  - `x in s`, `s <= t` (is s a subset of t), `s - t`

- `collections.defaultdict`

  - Instantiated by specifying the value type

    ```python
    >>> import collections
    >>> d = collections.defaultdict(list)
    >>> s = [('a', 1), ('b', 2), ('a', 3), ('d', 4)]
    >>> for k, v in s:
    >>> 	d[k].append(v)
        
    >>> d
    defaultdict(<class 'list'>, {'a': [1, 3], 'b': [2], 'd': [4]})
    >>> d.items()
    dict_items([('a', [1, 3]), ('b', [2]), ('d', [4])])
    >>> d['a']
    [1, 3]
    >>> d['e']
    []
    ```

- `collections.Counter`

  - Used to count the number of occurrences of keys

    ```python
    >>> c = collections.Counter("abaa")
    >>> c
    Counter({'a': 3, 'b': 1})
    
    # Note that there are no quotation marks
    >>> d = collections.Counter(a=2,b=2,c=3,d=0)
    >>> d
    Counter({'c': 3, 'a': 2, 'b': 2, 'd': 0})
    
    # Only positive counts are presented
    >>> c + d
    Counter({'a': 5, 'b': 3, 'c': 3})
    
    >>> c - d
    Counter({'a': 1})
    
    >>> c & d
    Counter({'a': 2, 'b': 1})
    
    >>> c | d
    Counter({'a': 3, 'c': 3, 'b': 2})
    ```

- Operations on `dict`, `defaultdict`, `Counter`

  - `items()` - returns an iterator of key-value pairs
  - `values()` - returns an iterator of values
  - `keys()` - returns an iterator of keys

- Mutable containers are NOT hashable!

  - Can implement `__hash(self)__` in user-defined class