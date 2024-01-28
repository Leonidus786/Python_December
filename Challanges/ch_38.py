'''037 
Ask the user to enter their name and display each letter in 
their name on a separate line. 
038 
Change program 037 to also ask for a number. Display 
their name (one letter at a time on each line) and repeat this for the 
number of times they entered. '''


name = input("Enter Your name: ")

num = int(input("Enter a number: "))

#nesting of loops ---> do loop ek me lgana hai

for i in range(0, num):
    for c in name:
        print(c)