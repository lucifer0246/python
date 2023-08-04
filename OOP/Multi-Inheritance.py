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
                                    # AQUATIC INIT
print(captian.swim())               # PENGUIN INIT
print(captian.walk())               # Captain Cook is swimming
print(captian.greet())              # Captain Cook is walking
                                    # I am Captain Cook of the land!

print(isinstance(captian, Penguin))
print(isinstance(captian, Aquatic))
print(isinstance(captian, Ambulatory))
print(" ")




