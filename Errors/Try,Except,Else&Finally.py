#  while True:
#    try:
#        num = int(input("please enter a number: "))
#    except:
#        print("Thats not a number! ")
#    else:
#        print("I'm in the else! ")
#    finally:
#        print("Run no matter what! ")



def divide(a, b):
    try:
        result = a/b 
    except ZeroDivisionError:
        print("Don't divide by zero !")
    except TypeError:
        print("a and b must be ints or floats")
    else:
        print(f"{a} divided by {b} must be ints or floats i.e {a/b}")

print(divide(1, 2))
print(divide(1,'a'))