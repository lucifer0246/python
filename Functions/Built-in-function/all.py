# all

        # returns True if all the elements of the iterables are truthy (or if the iterable is empty)

print(all([0,1,2,3,4]))   # 0 - Flase, 1,2,3,4 - True
print(" ")

print(all([char for char in 'eio' if char in 'aeiou']))
print(" ")

print(all([num for num in [4, 2, 10, 6, 8] if num% 2 == 0]))
print(" ")

people =  ["chalie", "casey", "cody", "carly", "cristina"]
print(all([name[0] == 'c' for name in people]))