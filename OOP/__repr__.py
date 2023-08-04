# __repr__

        # represents the user/object data
        # the __repr__ method is one of the several ways to provide a nicer sting representation

class User:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first} is {self.age}"
    
    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

tom = User.from_string("Tom,Jones,89")
print(tom)   # Tom is 89
print(" ")


class Human:

    def __init__(self, name = "somebody"):
        self.name = name
    
    def __repr__(self):
        return self.name

sam = Human()
print(sam)  # somebody