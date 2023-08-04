# Moderator and User

        # Moderator are active, they are simply user they have some additinal functionality like deleting a post, hiding them delete comment

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

    def logout(self):                              
        User.active_user -= 1                      
        return f"{self.first} has logged out"  
    

class Moderator(User):

    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods"
    
    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"
    

jasmine = Moderator("jasmine", "conner", 61, "piano") 

print(jasmine.full_name())

print(jasmine.community)
print(" ")

print(User.display_active_users())
user1 = User("joe", "smith", 68)
print(User.display_active_users())
jasmine2 = Moderator("jasmine", "conner", 61, "piano") 
print(User.display_active_users())
print(" ")

user1 = User("joe", "smith", 68)
user2 = User("joe", "smith", 68)
user3 = User("balanca", "lopez", 41)
user4 = User("balanca", "lopez", 41)
jasmine3 = Moderator("jasmine", "conner", 61, "piano") 

print(User.display_active_users())
print(Moderator.display_active_mods())