# any --

        # returns True, if any element of the iterable is truthy
        # if the iterable is empty, returns False

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(any([num % 2 == 1 for num in nums]))
print(" ")

print(any([num % 2 == 0 for num in nums]))
print(" ")

print(any([num % 2 == 2 for num in nums]))
print(" ")

