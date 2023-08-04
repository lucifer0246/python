# list
# syntax =>
#  a = ["string", True, 1, 1.233, [1, 2.43, 12]]

a = [1, 2, 3, 4, "hii"]
print(a)                                #[1, 2, 3, 4, "hii"]

length = len(a)
print(length)                           #5

task = list(range(1,4))
print(task)                             #[1, 2, 3]

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)                            #["apple", "banana", "cherry"]

t  = type(task)
print(t)                                #<class 'list'>

print(" ")

# Indexing :-
friends = ["Ashely", "Matt", "Michael"]
print(friends[0])                       #Ashely

print(friends[1])                       #Matt 

print(friends[-1])                      #Michael

print(friends[-3])                      #Ashely

print(" ")


num = [1, 2, 3, 4, 4, 4, 5, 5, 5, 10]
print(num.index(3))                            
print(num.index(4, 5))      
print(num.index(5, 5, 8))                  
# provides index of number as output
# privide index of 4 after the index 5(5 inclusive)
# .index(value, after index, before index)
print(" ")


# Checking values in list "in"

friends = ["Ashely", "Matt", "Michael"]
print("Ashely" in friends)
print("Matt" in friends)
print("sam" in friends)