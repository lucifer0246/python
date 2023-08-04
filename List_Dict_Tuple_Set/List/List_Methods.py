# 1) .append()

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6, 7]) # type: ignore
print(a)
print(" ")

# print(a.append(5, 6, 7))  
# TypeError: list.append() takes exactly one 




# 2) .extend()

b = [1, 2, 3]
b.extend("hi") # type: ignore
print(b)

# b.extend(2) # type: ignore
# print(b)    # TypeError: 'int' object is not iterable

b.extend("2") # type: ignore
print(b)

b.extend([4, 5, 6])
print(b)
print(" ")





# 3) .insert()        .insert( index, value)

first = [1, 2, 3, 4]
first.insert(2, "HI") # type: ignore
print(first)
print(" ")



# 4) .clear()

f = [1, 2, 3, 4]
print(f)
f.clear()
print(f)

# c = [1, 3, 1, 1, 1]
# c.clear(2)           #TypeError: list.clear() takes no arguments (1 given)
print(" ")



# 5) .pop()

p = [1, 2, 3, 5, a]

print(p)
p.pop()      # by defult last value
print(p)
p.pop()
print(p)
print(" ")




# 6) .remove()

h = [1, 2, 3, 3, 4, 4, 5, 4]
h.remove(4)    # removes 1st 4 that comes
print(h)
h.remove(4)
print(h)
print("")




# 7) .count()

num = [1, 2, 3, 3, 3, 3, 4, 4, 4]         # returns the count of specific element in list
print(num.count(3))

print(num.count(4))
print(" ")




# 8) .reverse()

first = [1, 2, 3, 4, 5]
first.reverse()

print(first)
print(" ")




# 9) .sort()

a = [3, 66, 12, 10, 1, 2]
a.sort()
print(a)
print(" ")



# 10) .join()

words = ['coding', 'is', 'fun']                  # converting list into string
print(words)             # ['coding', 'is', 'fun']  
print(' '.join(words))   # 'coding is fun'
print(''.join(words))    # 'codingisfun'
print(" ")




# 11) slice

l = [1, 3, 4, 6, 8, 9]              # creates the list from existing list
l1 = l[:]                           # new = old[ after : before : step ]
print(l1)     #[1, 3, 4, 6, 8, 9]

l2 = l[1:]
print(l2)     #[3, 4, 6, 8, 9]

l3 = l[3:]
print(l3)      #[6, 8, 9]

l4 = l[2 : 5 ]
print(l4)     #[4, 6, 8]

l5 = l[-5 : -2]
print(l5)     #[3, 4, 6]

l6 = l[ : 3]
print(l6)   #[1, 3, 4]
print(" ")




# 12) swapping

name = ["Jame", "Michelle"]
print(name)
name[0], name[1] = name[1], name[0]

print(name)
