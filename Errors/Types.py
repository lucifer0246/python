# 1) SyntaxError - 
        # occurs when python encounters incorrect syntax(something it doesn't parse)

# def first:  # SyntaxError: expected '('
# None = 1     # SyntaxError: cannot assign to None
# return     # SyntaxError: 'return' outside function



# 2) NameError -
        # This occurs when a variable is not defines i.e. its hasn't been assigned

# test       # NameError: name 'test' is not defined



# 3) TypeError - 
        # An operation or function is applied to the wrong type
        # python can't interpret an opertion on two datatypes

# len(5)      #TypeError: object of type 'int' has no len()
# "awsome" + []   # TypeError: can only concatenate str (not "list") to str



# 4) IndexError -
        # occurs when you try to access an element in a list using invalid index

# list = ['hello']
# list[2]         # IndexError: list index out of range



# 5) ValueError - 
        # This occurs when a built-in operation or function receives argument that has the right type but inappropriate value

# int("foo")    # ValueError: invalid literal for int() with base 10: 'foo'



# 6) KeyError - 
        # This occurs when a dictionary does not a specific key

# d = {}
# d['foo']   # KeyError: 'foo'



# 7) AttributeError - 
        # This occurs when a variable does have an attribute

# "awsome".foo     # AttributeError: 'str' object has no attribute 'foo'


