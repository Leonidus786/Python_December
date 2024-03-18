'''078 
Create a list containing the titles of
four TV programmes and display 
them on separate lines. Ask the 
user to enter another show and a 
position they want it inserted into 
the list. Display the list again, 
showing all five TV programmes in 
their new positions. '''

my_tv_shows = ["Man vs Wild", "Top Guns","Sea Hawk","Game of Thrones"]

for i in my_tv_shows:
    print(i)
print() # For making a space below our list

new_tv_show = input("Enter Another TV show: ")
Show_position = int(input("Enter a number between 0 and 3: "))

my_tv_shows.insert(Show_position,new_tv_show)

for i in my_tv_shows:
    print(i)