# print

print("hello")
print(" ")
print(4)
print(" ")
print(4+5)
print(" ")

# numbers and float type() function
print(type(4))
print(" ")
print(type(3.444))
print(" ")

# No need to chnage float into int or vice verca before performing any operation
print(3 + 3)    # int + int  = int
print(" ")

print(3.3 + 3)   # float + int = float
print(" ")

print(3.3 + 3.3)  # float + float = float 
print(" ")

print(5/4)        # int / int = float or int
print(" ")


# variable and Datatypes

x = 100
print(x)
print(" ")

total_value = 500
print(total_value)
print(" ")

all, at, once = 5, 10, 15
print(once)
print(all)
print(at)
print(" ")

a = b = c = 300
print(a, b, c)
print(" ")

print(id(a))
print(id(b))
print(id(c))
print(" ")

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)
print(" ")

# Name convenction

     # Variables       =  no starting with integer 
     # ALL CAPITAL     =  constants
     # UpperCamelCase  =  class name
     # _no_touchy_     =  private not to be changed

# Reserved key words

    # False        def      if         raise
    # None         del      import     return
    # True         elif     in         try
    # and          else     is         while
    # as           except   lambda     with
    # assert       finally  nonlocal   yield
    # break        for      not
    # class        from     or
    # continue     global   pass


# Datatype

x = True    # Boolean  True or False
print(x)
print(" ")

print(1)           # Integer

print(1.333)       # Float

print(" Hello! nice to meet you ")  # String

print(['hi', 2, [1, 2, 3]])     # List

x = ['hi', 2, [1, 2, 3]]     # List
print(x)

a = {'first':'harry', 'last':'potter'}   # Dict
print(a)
print(" ")


# Dynamic Typing
awsome = 5   # we can assig different values of different datatypes to single valrible, which is possible in python but not in c++
print(awsome)

awsome = "GREAT"
print(awsome)

awsome = True
print(awsome)
print(" ")


# None
child = None
print(child)
print(type(child))
print(id(child))
print(" ")


# \n
a = "Hello \nworld!"
print(a)
print(" ")

# "....."
a = "Rahul said \"This is my chance\""
print(a)
print(" ")

# string concatenation
str1 = "Your"
str2 = "name"
str3 = "is"
q = str1 + " " + str2 + " " + str3
print(q)

str1 = "ice"
str1 += "cream"
print(str1)        # Note = we cannot concatente integer and string, we can use integer by changing datatype of integer
print(" ")


# formatting string
x = 10    # adding integer or varible inside the string
string = f"i have {x} apple"
print(string)
print(" ")


# string indexing
name = "sam"        # Indexing start with zero and spaces have index value
print(name[0])
print(name[2])
print(name[-2])
print(name[-1])
print(" ")

# conveting datatypes
decimal = 2.23422
print(decimal)
print(int(decimal))
print(decimal)
print(" ")

my_list = [1, 2, 3]
print(my_list)
print(str(my_list))
print(type(str(my_list)))








