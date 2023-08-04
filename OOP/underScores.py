# _name

        # This is intended for internal use
        # use only inside the class
        # It will work outside but good to use only inside the class
class Test:

    def __init__(self):
        self.name = "datacamp"
        self._num = 7

obj = Test()
print(obj.name)
print(obj._num)
print(" ")


# __name

        # used for name mangling
        # name mangling - interpreter of the python alters the variable name in a way that is challenging to clash when the class is inherited

class Sample():

    def __init__(self):
        self.name = 1
        self._secret = 2
        self.__msg = 3
        self.__lol = 4

obj1 = Sample()
print(dir(obj1))
print(" ")

class Person():
        def __init__(self):
                self.name = "tony"
                self._secret = "hill"
                self.__msg = "I like football"
                self.__lol = "HAHAHAHAHA"
        
        def get_msg(self):
            return self.__msg

        def get_lol(self):
            return self.__lol

p = Person()

print(p.name)
# print(p._secret)
# print(p.__lol)
print(" ")
print(dir(p))
# print(p.__msg)  # AttributeError: 'Person' object has no attribute '__msg'
# print(p.__lol)  # AttributeError: 'Person' object has no attribute '__lol'
print(" ")

print(p.get_msg())               
print(p.get_lol())  