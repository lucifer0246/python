# Given the list of names, return a new list with the sting "your instructor is " + each value in 
# list but if the value is less than 5 charachters

name = [ "lassie", "colt", "rusty", "sam"]

l = list(map(lambda na : f"Your instructor is {na}" ,
             filter(lambda value : len(value) < 5 , name)))

print(l)