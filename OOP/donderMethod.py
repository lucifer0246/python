# special method / donder method

        # if the first(left) operant is an instance of int, __add__() does mathematical addition. if its a string, it does string concatention

print(8 + 2)
print("8"+"2")
print(" ")

class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first = "Newborn", last = self.last, age = 0)
        return "You can't add that!"
    
    def __mul__(self, other):
        if isinstance(other, int):
            return [Human(first=self.first, last=self.last, age=self.age) for i in range(other)]
        return "Can't multiply"

j = Human("jenny", "larsen", 47)
k = Human("kevin", "jones", 49)

print(j)
print(len(j))
print(" ")

print(j+k)
print(j+2)
print(" ")

print(j*2)
print((j+k)*2)
print(" ")

triplet = j*3
print(triplet)
