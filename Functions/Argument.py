def full(first, second):
    return(f"your full name is {first} {second}")

print(full("sam", "watson"))       # sam and watson are the arguments that we pass into function
print(" ")

# keyword argument

def full1(first, last):
    return(f"your full name is {first} {last}")
print(full1(first ="colt", last = "jackson"))
print(full1(last = "jackson", first = "colt"))
print(" ")




# *args

         # a special operator we can pass to function
         # gather remaining arguments as a tuple

def sum(num1, num2, num3, num4 = 0, num5 = 0):         #  when we need to provide more no of arguments it won't be good way to provide multiple  argument
    return num1 + num2 + num3 + num3 + num4 + num5

# sum(2, 3, 4, 7, 7, 7, 8)   # TypeError: sum() takes from 3 to 5 positional arguments but 7 were given
sum(2, 3, 4, 7, 7)
sum(2, 3, 4, 7)
print(" ")

def sum1(*args):
    print(args)
sum1(2, 3, 4, 5, 4, 5)
print(" ")


def sum2(*args):
    total = 0
    for num in args:
        total += num
    return print(total)

sum2(2, 4, 5, 5, 6)
print(" ")

def correct(*args):
    if "colt" in args and "steels" in args:
        return "welcome back colt!"
    return "not sure who you are..."

print(correct())
print(correct("colt","steels"))
print(" ")




# **kwargs 

        # take as key-value pair argument
        # a special operator we can pass to function
        # input as dictonary for arrgument for a function call

def fav_colors(**kwargs):
    print(kwargs)
fav_colors(colt = "purple", ruby = "red", ethel = "teal")

def fav(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
fav(colt = "purple", ruby = "red", ethel = "teal")

def special(**kwargs):
    if "Devid" in kwargs and kwargs["Devid"] == "special" :
        return "You get a special greeting Devid"
    elif "Devid" in kwargs:
        return f"{kwargs} Devid!"
    return "Not sure who is this"

special(Devid="hello")
print(" ")



# parameter ordering

        # 1) parameters
        # 2) *args
        # 3) default parameters
        # 4) **kwargs

def display_info(a, b, *args, instructor = "colt", **kwargs):
    return print([a, b, args, instructor, kwargs])

display_info(1, 2, 3, "sam",last_name = "steele", job = "instructor")
print(" ")


# using  *  as an argument : (Argument unpacking)
     
      # we can use * as an argument to function to "unpack" values

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total) 

num = [1, 2, 3, 4, 5, 6]
sum_all_values(*num)
print(" ")


# using  **  as an argument : (Dictionary unpacking)

def add_and_multi(a, b, c, **kwargs):
    print(a+b*c)
    print("other stuff.....")
    print(kwargs)

data = dict(a = 1, b = 2, c = 3, d = 5, name = "Tony")

add_and_multi(**data)
