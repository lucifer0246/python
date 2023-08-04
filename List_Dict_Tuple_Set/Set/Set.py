#  sets cannot have duplicates value
#  element in sets are not ordered
#  you cannot access items in a set by index
#  sets can be useful if you need to keep track of collection of elements, but don't care about ordering, key or values and duplicates

s = ({1, 2, 3, 4, 5})
print(s)
print(" ")

second = set({1, 2, 3, 4, 5})
print(second)
print(" ")

print(5 in s )
print(8 in s)
print(" ")


# assesing the data in sets

for things in s:
    print(things)


