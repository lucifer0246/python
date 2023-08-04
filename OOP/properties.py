# properties

        # earlier we need to define separate function for setting or getting value but with the properties we don't do that anymore

# earlier way

# class Human:
    
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last

#         if age >= 0:
#             self._age = age
#         else:
#             self._age = 0
        
#     def get_age(self):
#         return self._age
    
#     def set_age(self, new_age):
#         if new_age >= 0:
#             self._age = new_age
#         else:
#             self._age = 0
#         self._age = new_age
    

# jane = Human("jane", "goodall", -9)
# print(jane)         # <__main__.Human object at 0x00000213C627F290>

# print(" ")
# # print(jane.age)   # AttributeError: 'Human' object has no attribute 'age'. Did you mean: '_age'?

# print(jane.get_age())  # 0
# print(" ")

# jane.set_age(45)       # 45
# print(jane.get_age())



# new way

class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last

        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property    
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self,name):
        self.first, self.last = name.split(" ")

jane = Human("jane", "goodall", 34)
print(jane)         # <__main__.Human object at 0x00000213C627F290>

print(" ")
# print(jane.age)   # AttributeError: 'Human' object has no attribute 'age'. Did you mean: '_age'?

print(jane.age)  # 0
print(" ")

jane.age = 45       # 45
print(jane.age)
print(" ")

print(jane.full_name)
print(" ")

jane.full_name = "Tim Minchin"
print(jane.full_name)