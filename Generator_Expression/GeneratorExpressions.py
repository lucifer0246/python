# Generator Expression

        # generator expression look a lot like list comprehension
        # you can also create generators for generator expressions
        # generator exprssions use () instead of []

# before generator expression

# def nums():
#     for num in range(1, 10):
#         yield num

# g = (num for num in range(1, 10))
# print(next(g))        # 1
# print(next(g))        # 2
# print(next(g))        # 3
# print(next(g))        # 4


# after generator expression
g = (num for num in range(1, 10))
print(next(g))   # 1
print(next(g))   # 2
print(next(g))   # 3
print(next(g))   # 4
print(" ")

# list comprehension
l = [num for num in range(1, 10)]
print(l)
print(" ")

# with list comprehension
s = sum([sum for sum in range(1, 10)])
print(s)
print(" ")

# with generator expressions
k = sum(sum for sum in range(1, 10))
print(k)