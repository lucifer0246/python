#  __name__      (known as donder)

        # when runs, every python file has a __name__ variable
        # if the dile is the main file being run, its value is "__main__", otherwiase, its file name


import file1

def say_hi():
    print(f"Hi this is {__name__}")
    return say_hi

say_hi()
file1.name()