# Writing a Beat making Generator

# without generator

# def current_beat():
#     max = 10
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []

#     while len(result) < max:
#         result.append(nums[i])
#         i = (i + 1) % len(nums)

#     return result

# print(current_beat())


# with generator

def current_beat():
    max = 10
    nums = (1, 2, 3, 4)
    i = 0
    count = 0

    while count < max:
        yield nums[i]
        i = (i + 1) % len(nums)
        count += 1

counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(" ")

# Using a loop to iterate over the generator and print each value
# for beat in current_beat():
#     print(beat)
# print(" ")

# 1
# 2
# 3
# 4
# 1
# 2
# 3
# 4
# 1
# 2

# Alternatively, you can convert the generator to a list and then print the list
result = list(current_beat())
print(result)     # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]

