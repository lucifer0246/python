a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

print(a[0][2])    #3
print(a[1][1])    #5
print(a[2][2])    #9
print(" ")


# acessing each and every element in nested list
for l in a:
    for value in l:
        print(value)
print(" ")


# nested list comprehension
a = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
b = [[print(val) for val in l] for l in a]
# print(b)   # [[None, None, None], [None, None, None], [None, None, None]]