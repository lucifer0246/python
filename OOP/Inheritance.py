# Inheritance

        #  A key feature of oop is the ability to define a class which inherits from another class (a "base" or "parent" class)
        # In python, inheritance works by passing parent class as ana arrgument to the definition of child class

class Animal:
    cool = True

    def make_sound(self, sound):
        print(sound)
    
class Cat (Animal):
    pass

gandalf = Cat()
gandalf.make_sound("meow")

print(gandalf.cool)

print(isinstance(gandalf, Cat))
print(isinstance(gandalf, Animal))
