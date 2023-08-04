# lambdas --- are the built in function

        # special case function
        # anonomus function
        # single line function that is automatically return

# normal function
def square(num):return print(num*num)
square(7)
print(" ")

# lambda function
# func_name = lambda  parameter : body of function
square2 = lambda num : print(num * num)
square2(5)
print(" ")

add = lambda a,b : print( a + b)
add(2, 3)
print(" ")

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)
