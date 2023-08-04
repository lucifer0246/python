#  a parameter is a variable in method definition or function definition

def add2(a,b):        # here a and b are parameter
    return a+b

print(add2(4, 5))
print(" ")


def multipy(first, second):
    return first * second
print(multipy(4, 5))
print(" ")



# default parameter

def exponent(num, power = 2):       # power = 2 is a default parameter that we pass to any function
    return num**power

print(exponent(3))
print(exponent(4, 3))
print(" ")

# def add(a, b):
#   return a+b
# print(add(2))                       # throws error (add() missing 1 required positional argument: 'b')

def add1(a=4, b=2):
    return a+b
print(add1())
print(add1(4, 11))
print(" ")


def add(a,b):
    return a+b
def math(a, b, fn = add):
    return fn(a,b)
def substract(a,b):
    return a-b
print(math(2, 3))
print(math(2, 2, substract))
print(add(1, 2))
