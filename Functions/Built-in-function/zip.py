first = zip('abcdefg', range(3), range(4))
print(first)
print(" ")

print(list(first))
print(" ")


five_by_two  = [(0,2),(22,45),(23, 55),(57, 34),(33, 123)]
print(list(zip(* five_by_two)))
print(" ")


second = zip([1, 2, 3],[4, 5, 6])
print(list(second))
second = zip([1, 2, 3],[4, 5, 6])
print(dict(second))