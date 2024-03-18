"""Local scope: The names that you define in this scope are only 
available or visible to the code within the scope.
"""

# def myfunc():
#     x = 9 #local scope mtlb sirf myfunc() ke andar use hoga
#     print(x)


# myfunc()




def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# print(x)
