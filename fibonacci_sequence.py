# fibonnacci sequence - 1, 1, 2, 3, 5, 8, 13, .................

# without generator 

# def fib_list(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max :
#         nums.append(b)
#         a, b = b, a+b
#     return nums

# print(fib_list(10))


# with generator

def fib_gen(max):
    x =0
    y = 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1

for n in fib_gen(20):
    print(n)
print(" ")

print(fib_gen(10))
