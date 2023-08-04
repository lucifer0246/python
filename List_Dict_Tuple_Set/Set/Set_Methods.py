# 1) .add()

s = set([1, 2, 3, 3, 3, 3, 1, 2,])
print(s)

s.add(4)
print(s)
print(" ")




# 2) .copy()

s= ([1, 2, 3])                 # creates a copy od sets
s_copy = s.copy()

print(s_copy is s)
print(s_copy)
print(s)
print(" ")



# 3) .clear()

s = ({1, 2, 3})                # removes all the content of set
print(s)

s.clear()
print(s)

a = ({})
print(a)