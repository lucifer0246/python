# Method Resolution Order(MRO)

        # whenever, you create a class, python Sets a method resolution order, or MRO, for that class, which is the order in which python will look for methods as instances of that class

# find theMRO of the class

        # __maro__ attribute on the class
        # use the mro() method on the class
        # use the builtin help(cls) method

class Aquatic:

    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name
    
    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"    
    
# class Penguin(Ambulatory, Aquatic):          # Here sequence of parameter matters

#     def __init__(self, name):
#         print("PENGUIN INIT")
#         super().__init__(name = name)

class Penguin(Ambulatory, Aquatic):          # Here sequence of parameter matters

# note- if need to run both Ambulatory and Aquatic
    def __init__(self, name):
        print("PENGUIN INIT")
        Ambulatory.__init__(self, name = name)
        Aquatic.__init__(self, name = name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captian = Penguin("Captain Cook")

print(Penguin.__mro__)
print(" ")
print(Penguin.mro())
print(" ")
print(help(Penguin))
print(" ")


class A:
    
    def do_something(self):
        print(" Method define in A")

class B(A):

    def do_something(self):
        print(" Method define in B")

class C(A):

    def do_something(self):
        print(" Method define in C")

class D(B,C):

    def do_something(self):
        print(" Method define in D")


thing = D()
thing.do_something()
print(" ")

print(D.__mro__)
print(" ")
print(D.mro())
print(" ")
print(help(D))
print(" ")


    