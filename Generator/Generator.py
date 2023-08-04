#  Generator

        # Generator are iterators
        # gernrator can be created with generator function
        # generator function use the yeild keyword
        # generator can be created with genaertor expressions

# function vs gernerator function

# -----------------------|-------------------------------------
#         function       |       generator function
# -----------------------|-------------------------------------
#       use return       |        use yield
#                        |
#       return once      |     can yield multiple time
#                        |
#  when invoked, returns |   when invoked, returns a generator
#    the return value    |
# -----------------------|-------------------------------------

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(counter)
# print(counter())      # TypeError: 'generator' object is not callable
print(next(counter))    # 1
print(next(counter))    #
print(next(counter))    #
print(next(counter))    #
print(next(counter))    #
print(" ")

counter = count_up_to(10)
for num in counter:
    print(num)
    pass
print(" ")

counter = count_up_to(10)
print(list(counter))
