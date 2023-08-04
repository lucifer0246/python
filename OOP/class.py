# oop

        # oop  is a method for programming that attempts to model some process or thing in the world as a class or object

# why oop?

        # with oop the goal is to encapulate your code into logical , hierarcial grouping using classes so that you can reason about your code at a higher level

# class

        # classes are the blueprint for object, classes can contain methods(functions) and attributes(similar to keys in dict)

# instance

        # objects that are constructed from a class blueprint that contain their class method and properties

# Encapsulation

        # the grouping of public nd private attributes and methods into programmatic class, making abstraction possible
        # it describe the idea of wrapping data and the methods that work on data within one unit

# abstraction

        # exposing only "relevant" data in a class interface, hiding the private attributes and methods (aka the "inner working") from users.

# class creation

        # syntax -
        #           class ClassName:    
        #               pass               ->terminate class

# onject/instance creation from class

        #   object name <-  user1 = User()  -> class name
        # print(type(user1))    # <class '__main__.User'>

# __init__

        # class python have a special __init__  method, which gets called every time you create an instance of the class(instantiate)

class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year                # (self.year) -> name of attribute      (year)  -> value
        pass

class   Dog:

    def __init__(self, dogBreed, dogEyeColor):
        self.breed = dogBreed
        self.eyeColor = dogEyeColor
        pass


class User:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("joe", "smith", 68)
user2 = User("blanca", "lopaez", 41)

print(user1.first, user1.last)
print(user2.first, user2.last)
print(" ")




