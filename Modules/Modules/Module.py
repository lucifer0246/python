# modules-

        # There are built in modules in python eg. random
        # already exist  just need to import
        # does not need to download specialy

import random   # module

print(random.choice(["apple", "banana", "cherry", "orange"]))         # random method
a = random.shuffle(["apple", "banana", "cherry", "orange"])
print(a)
print(" ")


# renaming the module (rename only if module name is large)
import random as omg_random  



# from

        # "From" keyword lets you import what you need from the module

from random import choice,randint
print(choice(["apple", "banana", "cherry", "orange"]))
print(randint(1, 1000))



# Different ways of importing

import random
import random as omg_random
from random import *               # type: ignore
from random import choice, shuffle
from random import choice as ch, shuffle as sh
