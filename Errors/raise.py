
# raise ValueError("invalid value")

# raise ValueError

# raise NameError('blahhha')


def colorize(text, color):
    colors = ('cyan','yellow','blue','green','magenta')

    if type(text) is not str:
        raise TypeError("Text must be instance of string")
    if color in colors:
        print(f"Printed {text} in {color} ")
    else:
        raise ValueError("Color not present in colors")

colorize("hello", "blue")