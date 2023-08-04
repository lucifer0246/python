# map

        # A stanard function that accepts at least two arrguments, a "function" and an "iterable"
        # An "iterable" is something that can be iterated over eg(list, string, dict, sets, tuples)
        # Runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

num = [2, 4, 6, 8, 10]
f1 = lambda x : x * 2
double = map(f1, num)
print(list(double))       # shows output for the single time only similar to generator function
print(" ")

print(double)
print(" ")

num = [2, 4, 6, 8, 10]
f1 = lambda x : x * 2
double = map(f1, num)
for num in double:
    print(num)
print(" ")

names = [
    {"first" :"Rusty" , "last":"steele"},
    {"first" :"blue", "last":"steele"},
    {"first" :"colt" , "last":"steele"}
    ] 
first_name = list(map(lambda x : x["first"], names))
print(first_name)
