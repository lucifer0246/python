class Human:

    def __init__(self, name = "somebody"):
        self.name = name
    
    def __str__(self):
        return self.name

sam = Human()
print(sam)       # somebody