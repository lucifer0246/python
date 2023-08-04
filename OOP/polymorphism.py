# polymorphism

        # A key principle in oop is the idea of polymorphism- an object take on many(poly) forms(morph)

# Applications of polymrphism

# 1) the same class method works in a similar way for different classes

        # a common implementation of this is the to have a method in a base(or parent) class that is overriden by subclass. this is called method overriding
        # Each subclass will have different implementation of method

class Animal:
    
    def speak(self):
        raise NotImplementedError(" Subclass needs to impelement this method")

class Dog(Animal):

    def speak(self):
        return "woof"

class Cat(Animal):

    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()

print(d.speak())
print(" ")

c = Cat()
print(c.speak())
print(" ")

f = Fish()
# print(f.speak())     # NotImplementedError:  Subclass needs to impelement this method

# 2) The same operation works for different kinds of object

        # python class have special (also called as "magic") method, that are dunders (i.e. double underScore_named)
        # there are methods with special names that give instructions to python for (how to deal with objects)

sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)
sample_string = "awsome"

print(len(sample_list))
print(len(sample_tuple))
print(len(sample_string))
print(" ")

print(8 + 2)
print("8" + "2")  