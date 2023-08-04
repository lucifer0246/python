# Debuging with pdb

        # To set breakpoints inour code we can use pdb by inserting this lines
        #       import pdb;     pdb.set.trace()


import pdb;
first = "first"
second = "second"
pdb.pm()
result = first + second
third = "third"
result += third
print(result)