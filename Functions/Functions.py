#   A process for executing a task
#   buch of line of code that would be required again and again in certian code, so we need functions
#
#   sometimes it accepts input and returns output
#   useful for executing similar process over and over
#
#   stay DRY
#  D = don't
#  R = repeat
#  Y = yourself
#
#  clean up and prevent code duplication


# syntax =>
#        def name_of_function():
#               code...........


def say_hi():
    print("hi")

say_hi()
# say_hi    # error function value is unused
print(" ")


# return (output side of the fuction)

      # uses:
      #    exits the function
      #    pops the function off the call stack

# def sequence():                     # no return value is provided by function
#    7**2

# result = sequence()                      
# print(result)      # none
# print(" ")

def sequence():                    # return value is provided by funtion
    return(7**2)

result = sequence()                      
print(result)

