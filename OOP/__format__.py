class Human:

    def __init__(self, name = "somebody"):
        self.name = name
    
    def __format__(self):
        return self.name

sam = Human()
print(sam)       # <__main__.Human object at 0x0000016DEA76EA50>