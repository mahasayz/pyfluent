## Python Data Model

Special methods invoked by the Python interpreter are always written with
leading and trailing double underscores, e.g. `__getitem__`

Syntax `obj[key]` is supported by `__getitem__`, interpreter calls `obj.__getitem__(key)`

> Special methods other known-as "dunder methods"

`namedtuple` used to create class of objects with only attributes and no custom methods.

> Implementing `__getitem__` and `__len__` makes the object iterable and by default supports features like slicing, random selection, etc.

#### TEST
__How do you select every 13th element from a list/iterable?__
> item[12::13]

If a collection has no `__contains__` method, `in` operation does a sequential scan.