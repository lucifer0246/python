# class method

        # class methods are methods (with the @classmethod decorator) that are not concerned with instances, but the class itself

class User:
    
    active_user = 0       

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_user} active users"                 
    
    def __init__(self, first, last, age): 
        self.first = first                         
        self.last = last                   
        self.age = age
        User.active_user += 1            

    def logout(self):                              
        User.active_user -= 1                      
        return f"{self.first} has logged out"  

user1 = User("joe", "smith", 68)
user2 = User("balanca", "lopez", 41)
print(User.display_active_users())
print(" ")

user3 = User("joe", "smith", 68)
user4 = User("balanca", "lopez", 41)
print(User.display_active_users())
print(" ")


# When we have csv file or datastring

class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return f"{self.first} {self.last}"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))
    

tom = Person.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
