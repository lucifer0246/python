a = 5           # "is" is True for same container
print(a is 5)   
print(a is 0)   


a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

c = b
print(b is c)

x = 13
y = 13
print(x == y)   # True
print(x is y)   # True (as we need not need to create new space for saving)

