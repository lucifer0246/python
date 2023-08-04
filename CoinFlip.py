#from random import randint
#def flip_coin():
#    randint(0,1)
    
from random import random

# def flip_coin():
#     r = random()
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

def flip_coin():
    if random() > 0.5:
        return print("Heads")
    else:
        return print("Tails")
    
flip_coin()