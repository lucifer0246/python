# outside the function
instructor = 'colt'

def say_hello():
    return f"Hello {instructor}"

print(say_hello())
print(instructor)
print(" ")


# inside the function

def say_hello1():
    instructor1 = "colt"
    return f"Hello {instructor1}"
print(say_hello1())
# print(print(instructor1))     # NameError: name 'instructor1' is not defined. Did you mean: 'instructor'?
print(" ")



# global scope

# total = 0
# def increment():
#    total += 1
#    return total
# print(increment())           #UnboundLocalError: cannot access local variable 'total' where it is not associated with a value

total1 = 0
def increment1():
    global total1
    total1 += 1
    return total1
print(increment1())



# nonlocal

# used in nested function
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

print(outer())
# print(inner())   #NameError: name 'inner' is not defined. Did you mean: 'iter'?
