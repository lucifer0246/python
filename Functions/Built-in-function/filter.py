# filter --

        # There is a lambda for each value to the terable
        # return filter object which can be converted into other iterable
        # The object contains only the values that returns true to the lambda

l = [ 1, 2, 3, 4]
even = list(filter(lambda x : x % 2 == 0, l))
odd = list(filter(lambda x : x % 2 != 0, l))

print(even)
print(odd)
print(" ")

name = ["austin", "penny", "anthony", "angel", "bily"]
a_name = list(filter(lambda n : n[0] == 'a', name ))
print(a_name)
print(" ")

users = [
    {"username": "samuel", "tweets": ["I love cat", "I love choclate"] },
    {"username": "katie", "tweets": ["i love cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob", "tweets": []},
    {"username": "doggo", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []},
    ]
inactive_user = list(filter(lambda u : len(u["tweets"]) == 0 , users))
print(inactive_user)
print(inactive_user[0])