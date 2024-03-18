thisset = {"apple", "banana", "cherry", "apple", True, 1}
# print(len(thisset))
# print("banana" in thisset)

'''What is difference between method and constructor in Python?
A constructor helps in initialising an object. A Method is a grouping of instructions that returns a value upon its execution.'''

#add() is a method


thisset.add("orange")

# print(thisset)

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
mylist = ["kiwi", "orange", "watermelon"]

mytuple = (1, 2, 3)

thisset.update(mylist)

thisset.update(mytuple)

#for removing an item we have two methods
thisset.remove("banana")
thisset.discard(True)

print(thisset)