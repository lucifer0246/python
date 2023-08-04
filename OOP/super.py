# super()

        # it is defined in child class for removing redundancy of code for accessing certain attribute of parent class

# earlier

# class Animal:

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def __repr__(self):
#         return f"{self.name} is a {self.species}"
    
#     def make_sound(self, sound):
#         print (f"this animal says {sound}")

# class Cat(Animal):

#     def __init__(self, name, species, breed, toy):
#         self.name = name
#         self.species = species
#         self.breed = breed
#         self.toy = toy

# blue = Cat("blue", "cat", "scotfish fold", "string")

# print(blue)             # blue is a cat
# print(blue.species)     # cat
# print(blue.breed)       # scotfish fold
# print(blue.toy)         # string



# After using super()

class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"
    
    def make_sound(self, sound):
        print (f"this animal says {sound}")

class Cat(Animal):

# 1st way with using super()

    # def __init__(self, name, species, breed, toy):
    #     super().__init__(name, species)
    #     self.breed = breed
    #     self.toy = toy

# 2nd way without keyword super()

    def __init__(self, name, species, breed, toy):
        Animal.__init__(self, name, species)
        self.breed =  breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = Cat("blue", "cat", "scotfish fold", "string")

print(blue)             # blue is a cat
print(blue.species)     # cat
print(blue.breed)       # scotfish fold
print(blue.toy)         # string
blue.play()
