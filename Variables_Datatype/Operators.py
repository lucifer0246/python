# Boolean and conditional logic

a = True   # only True not true
b = False  # only False not false
print(a)
print(b)
print(" ")

# by default value of 0 in flase 
print(False == 0)
print(True == 1)
print(" ")


# user input()
cash = input("Enter the amount :")
sam = "Enter the amount:"
input(sam)
print(" ")


#  Boolean Expressions
# 1) conditonal statement
          # syntax =>
          # if some condtion is True:
          #     do something
          # elif some other conditon is True:
          #     do something
          # else:
          #     do something or default output

name = input("Enter your name: ")
if name == "Aryan":
    print("Hello Aryan!")
elif name == "Sam":
    print("Hello Sam!")
else:
    print("You are imposter!")
print(" ")


x = 0               # "="  is for assinging the value
y = 5               # "==" is for boolean comparison

if y > x :
    print("yes")                  # Truthy

if y < x :
    print("yes")
else:
    print("no")                 # Falsy


if x:
    print("yes")               # Falsy by defult as assigned value in 0

if y:
    print("yes")               # Truthy by defult as some value is assigned to the variable

if 'aul' in 'grault':                # Truthy
    print('yes')
print(" ")


# 2) nested condition

age = input("Enter your age: ")
if age != "":
    if int(age) >= 18 and int(age) < 21:
        print("You can enter, but need a wristband")
    elif int(age) >= 21:
        print("You are good to enter and can drink")
    else:
        print("You can't come in, little one! :( ")
else:
    print("Please enter an age!")
print(" ")


