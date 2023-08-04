# use.value iterating over dictionary

instructor = {
    'name' : 'harry',
    'own_dog' : True,
    'no_courses' : 4,
    'fav_language' : 'python',
    'is_religious': False
}

print("value: ")
for value in instructor.values():
    print(value)
print(" ")

print("keys:")
for key in instructor.keys():
    print(key)
print(" ")


print("keys   values")
for value, key in instructor.items():
    print(f"{key} : {value}")
print(" ")

print(instructor.values())
print(" ")
print(instructor.items())


