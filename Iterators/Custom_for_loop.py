# creating custom for loop

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("End of Iterator!")
        
            break

my_for("hello")
print(" ")

# or
def m_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

m_for("lol", print)
print(" ")

m_for([1, 2, 3, 4, 5], square)