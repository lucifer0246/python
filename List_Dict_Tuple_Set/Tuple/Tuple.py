# an orderd collection or grouoing of items
# it is immutable (it can not be changed)

# first way
a = (1, 2, 3, 4)
print(a)
print(3 in a)
print(a[0])
# print(a[0] = 'b')    # SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print(" ")

# second way
second = tuple((1, 2, 3))
print(second)
print(" ")


location = {
    (35.6832, 39.2334) : "Tokyo Office",
    (40.1233, 12.3322) : "New York",
    (37.2323, 35.2233) : "San Francisco"
}

print(location)
print(location[(40.1233, 12.3322)])
print(" ")

cat = {'name': 'biscuit', "age": 10, "favorite_toy": "chess"}
print(cat)
print(cat.items())

