
"""Global scope: The names that you define in this scope are 
available to all your code.
"""
# x = 300 # Global variable --> khuli chut h kahi v access karlo pure program me



# def myfunc():
#   print(x)

# myfunc()

# print(x)



# x = 300

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)



# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x)

x = 300

def myfunc():
  global x
  x = 200  

myfunc()

print(x)
