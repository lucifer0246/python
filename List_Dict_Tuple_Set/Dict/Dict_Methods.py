# 1) .clear()

d = dict(a=1, b=2, c=3)
d.clear()
print(d)
print(" ")



# 2) .copy()

d = dict(a=1, b=2, c=3)
c = d.copy()

print(d)
print(c)
print(" ")



# 3) .fromkeys()

h = {}.fromkeys('a','b')      # initial it is empty
print(h)

h1 = {}.fromkeys('a',[1, 2, 3, 4, 5])
print(h1)

a = {}.fromkeys(['name', 'score', 'email', 'profile'], 'unknown')
print(a)
print(" ")




# 4) .get()

d = dict(a = 1, b = 2, c = 3)    # retrieves a key in an object and return none insted of KeyError if the key does not exist

print(d['a'])
print(d.get('a'))
print(d.get('d'))
print(" ")


# 5) .pop()

d = dict(a = 1, b = 2, c = 3)     # provide key for pop
print(d.pop('a'))
print(d)
print(" ")


# 6) .popitem()

d = dict(a = 1, b = 2, c = 3)     # pop random key-value pair
print(d.popitem())
print(d)
print(" ")


# 7)  .update()

list1 = dict(a = 1, b = 2, c = 3)
list2 = {}

list2.update(list1)
print(list2)

list2['b'] = 3
print(list2)

list2.update(list1)
print(list2)
print(list1)
print(" ")





