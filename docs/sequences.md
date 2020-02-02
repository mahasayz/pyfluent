## Sequences

There are 2 types:
* `container` sequences: Hold references to objects they contain e.g. list, tuple, collections.deque
* `flat` sequences: Store the value of each item e.g. str, bytes, memoryview, array.array

Another grouping is:
* __mutable__ sequences: list, bytearray, array.array, collections.deque
* __immutable__ sequences: tuple, str, bytes

`listcomps` are syntactic sugar for `map()` and `filter()`
```python
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127] # list comprehension
beyond_ascii = filter(lambda x: ord(x) > 127, map(ord, symbols)) # map and filter
```

> In certain situations, map() and filter() is faster than listcomps

`genexps` are efficient as they save memory by yielding items one by one instead of
generating the entire list.
```python
symbols = '$¢£¥€¤'
tuple(ord(s) for s in symbols)
# >>> (36, 162, 163, 165, 8364, 164)
import array
array.array('I', (ord(s) for s in symbols))
# >>> array('I', [36, 162, 163, 165, 8364, 164])
```

