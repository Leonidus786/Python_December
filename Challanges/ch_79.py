# pylint: disable=invalid-name


'''079 
Create an empty list called 'nums'. 
Ask the user to enter numbers. 
After each number is entered, add 
it to the end of the nums list and 
display the list. Once they have 
entered three numbers, ask them if 
they still want the last number they 
entered saved. If they say "no", 
remove the last item from the list. 
Display the list of numbers.'''

nums = []

count_no = 0

while count_no < 3:
    number = int(input("Enter a number: "))
    nums.append(number)
    print(nums)
    count_no = count_no + 1
last_num = input("Do you want the last number needs to be saved (y/n): ")

if last_num == "n":
    nums.remove(number)
print(nums)