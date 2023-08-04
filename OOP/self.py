# self

        # the self keyword refers to the current class interface
        # remember, the parameter doesn't have to called self, but it is standard and pretty much the only thing you will see
        # the self must always be the first parameter to __init__ and any methods and properties on class instances

class User1:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User1("joe", "smith", 68)
user2 = User1("blanca", "lopaez", 41)

print(user1.first, user1.last)
print(user2.first, user2.last)
print(" ")


# initiating new instances

class User:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        pass

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday {self.first}"
pass    
    

user3 = User("joe", "smith", 68)
user4 = User("blanca", "lopaez", 41) 

print(user3.likes("ice cream"))
print(user4.likes("chipps"))
print(" ")

print(user3.initials())
print(user4.initials())
print(" ")

print(user3.is_senior())
print(user3.age)
print(user3.birthday())
print(user3.age)
print(" ")

print(user3.full_name())
print(user4.full_name())