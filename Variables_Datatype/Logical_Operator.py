a = 12
b = 20

# 1) and operator

print(a > 10 and b < 22)              # and ^ (conjunction)  T^T = T
                               #                      T^F = F
                               #                      F^F = F
print(a < 10 and b < 22)
print(" ")



# 2) or operator

print(a > 10 or b < 22)             # or V (disjunction)   T V T = T
                             #                      T V F = T
                             #                      F V F = F

print(a < 10 or b > 22)
print(" ")


# 3) not operator

print(not a)
print(not b)
print(not (a > b))
