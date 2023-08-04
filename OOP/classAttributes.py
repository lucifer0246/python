# class attributes

        # we can also define attributes directly on a class that are shared by all instance of a class and the class itself

class User:
    
    active_user = 0                                # class variable
    
    def __init__(self, first, last, age):          # class instance
        self.first = first                         # instance attribute
        self.last = last                           # instance attribute
        self.age = age
        User.active_user += 1            

    def logout(self):                              # other instances
        User.active_user -= 1                      # other instances
        return f"{self.first} has logged out"    

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


print(User.active_user)
user1 = User("joe", "smith", 68)
user2 = User("balanca", "lopez", 41)
print(User.active_user)
print(user2.logout())
print(User.active_user)
