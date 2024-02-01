# #The try block will generate an error, because x is not defined:


# print(x)   # ---> ye mjhe error dega aur mera code rukega I don't want this.

# In order to avoid a error I have to use try statement.


# try:
#   print(x)
# except:
#   print("An exception occurred")



#Print one message if the try block raises a 
#NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")