# higher order function

        # we pass a func as args to other funcs

def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

s = sum(3, square)
print(s)
print(" ")


from random import choice

# we can nest function inside one another

