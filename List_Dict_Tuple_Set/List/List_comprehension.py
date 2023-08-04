# syntax =>
#       [____for____in____]

nums = [1, 2, 3, 4]
print(nums)
print(" ")

y = [x * 10 for x in nums]
print(y)
print(" ")

z = [k/2 for k in nums]
print(z)
print(" ")

# looping way
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    double = num * 2
    doubled.append(double)

print(doubled)
print(" ")

# list comprehension way
number = [1, 2, 3, 4, 5]
dou = [x*2 for x in numbers ]
print(dou)
print(" ")

# examples =>

name = "colt"
n1 = [char.upper() for char in name]
print(n1)
print(" ")

n2 = [num * 10 for num in range(1,6)]
print(n2)                                         # range
print(" ")

n3 = [bool(val) for val in [0, [], " ", 1]]
print(n3)
print(" ")

print([x * 10 for x in nums])
print(" ")

numbers = [1, 2, 3, 4, 5]
print([str(num) for num in numbers])
print(" ")

# List comprehension with conditional logic

# use of only if
number = [1, 2, 3, 4, 5]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
print(even)
print(" ")
print(odd)
print(" ")

# use of if-else 
print([num * 2 if num % 2 == 0 else num/2 for num in number])
print(" ")


# use of string
with_vowel = "This is so much fun!"
v = " ".join(char for char in with_vowel if char not in "aeiou")
print(v)
print(" ")

