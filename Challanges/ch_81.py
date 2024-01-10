'''081
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
'''

subject_name = input("Enter your favourite subject: ")

for letter in subject_name:
    print(letter, end = '-')