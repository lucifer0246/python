# Iterator Vs Iterables

        # Iterator - an object that can be iterated upon, an object which returns data one element at a time when next() is called on it.
        # Iterable - an object which will return an iterator iter() is called on it
        # next() - When next() is called on an iterator, the iterator returns the next item. it keeps doing so until it raises a StopIteration error


name = "Oprah"
# next(name)         # TypeError: 'str' object is not an iterator

it = iter(name)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))       # StopIteration
print(" ")

nums = [1, 2, 3, 4, 5]
# next(nums)              # TypeError: 'list' object is not an iterator

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))             # StopIteration
