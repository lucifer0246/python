# 1st way of creating
instructor = {
    'name' : 'harry',
    'own_dog' : True,
    'no_courses' : 4,
    'fav_language' : 'python',
    'is_religious': False
}

# 2nd way of creating
second = dict(
    name = 'harry',
    own_dog = True,
    no_courses = 4,
    fav_language = 'python',
    is_religious = False
)

print(instructor["name"])
# print(instructor["thing"])   # KeyError: 'thing'

print(second["own_dog"])
print(" ")


# checking key values exist or not

print("name" in instructor)
print("harry" in instructor)
print("name" in instructor)