"""Errors and Exceptions"""  
#Type 

#1. Syntax Error --> Parsing Error

# while True print('Hello world')

# Exceptions  -->

# print(10 * (1/0))
# print(4 + spam*3)
# print('2' + 2)


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")




