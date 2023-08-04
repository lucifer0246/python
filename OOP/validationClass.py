# validation with class variables

class Pet:
    allowed = ["cat", "dog", "fish", "rat"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError (f"You have {species} as pet!!")
        
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError (f"You have {species} as pet!!")


cat = Pet("blue", "cat")
print(cat.species)
print(" ")

# cat.set_species("tiger")               # ValueError: You have tiger as pet!!

cat.set_species("rat")
print(cat.species)
print(" ")

print(Pet.allowed)
print(" ")

Pet.allowed.append("pig")
print(Pet.allowed)
print(" ")

print(id(cat.allowed))
print(id(Pet.allowed))
