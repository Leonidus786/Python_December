# # my_dict = {'name':'Abhishek', 'Roll No': 55, 'Add':'XYZpur'}

# # print(my_dict['name'])

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964,
# #   "year": 2020
# # }
# # print(thisdict)

# # thisdict = {
# #   "brand": "Ford",
# #   "electric": False,
# #   "year": 1964,
# #   "colors": ["red", "white", "blue"]
# # }

# # print(thisdict)


# # thisdict = dict(name = "John", age = 36, country = "Norway")
# # print(thisdict.keys())

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# # x = car.keys()

# # print(x) #before the change
# # print(car)

# car["color"] = "black"

# # print(x) #after the change

# # y = car.values()

# # print(y)

# # z = car.items()
# # car["year"] = 2020

# # print(z)

# a=car.update({"year": 2022})

# # car.pop("year")

# # car.popitem()

# # del car

# # car.clear()

# # print(car)

# # for i in car:
# #     print(car[i])

# # for x, y in car.items():
# #   print(x, y)

# mydict = car.copy()
# print(mydict)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# print(myfamily)

print(myfamily["child2"]["name"])



