print(max(3, 67, 99))
print(" ")

print(max('d', 'c', 'a'))
print(" ")

print(max([3, 4, 1, 2]))
print(" ")

print(max((1, 2, 3, 4, 5, 6)))
print(" ")

print(max('awsome'))
print(" ")

print(max({1 : 'a', 3 : 'c', 2 : 'z'}))
print(" ")

names = [ 'ayra', 'samson', 'dora', 'trim', 'oliver']
print(min(len(names) for name in names))
print(" ")

print(max(names, key = lambda n : len(n)))
