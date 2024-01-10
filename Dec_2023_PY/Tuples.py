# Tuples--> tuples()


# my_tuple = (1, 2, 3, "Abhishek", True, False, 22.5)

# my_tuple_1 =(3+2j, 'K', "Mango",[1,2,3,"Alisha"])

# print(my_tuple[3])

# print(my_tuple_1[-1])

# my_tuple[2] = 4 --> we can't do it 

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# print(len(my_tuple_1))

# thistuple = ("apple",)
# print(type(thistuple))

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

my_tuple = (1, 2, 3, "Abhishek", True, False, 22.5)

my_tuple_1 =(3+2j, 'K', "Mango",[1,2,3,"Alisha"])

# print(len(my_tuple))
# print(my_tuple[2:7])

x = list(my_tuple_1)

x[3] = 'Alisha'

my_tuple_1 = tuple(x)

my_tuple += my_tuple_1

# print(len(my_tuple))
# print(my_tuple)

# (a,b,*c,d,e) = my_tuple

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# looping through each item
# for i in my_tuple:
#     print(i)

# Looping through Index
for i in range(len(my_tuple)):
    print(my_tuple[i])


