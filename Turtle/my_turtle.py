import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle named 'my_turtle'
my_turtle = turtle.Turtle()

# Move the turtle forward by 100 units
my_turtle.forward(100)

# Turn the turtle left by 90 degrees
my_turtle.left(90)

# Move the turtle forward by 100 units
my_turtle.forward(100)

# Close the turtle graphics window when clicked
screen.exitonclick()


"""
turtle.Screen(): Creates a turtle graphics window.
turtle.Turtle(): Creates a turtle named my_turtle.


my_turtle.forward(100): Moves the turtle forward by 100 units.
my_turtle.left(90): Turns the turtle left by 90 degrees.

my_turtle.forward(100): Moves the turtle forward by 100 units.

You can experiment with various turtle commands to create different shapes and patterns. Here are some commonly used turtle commands:

forward(distance): Move the turtle forward by a specified distance.
backward(distance): Move the turtle backward by a specified distance.
right(angle): Turn the turtle right by a specified angle in degrees.
left(angle): Turn the turtle left by a specified angle in degrees.
penup(): Lift the pen (stop drawing).
pendown(): Lower the pen (start drawing).
goto(x, y): Move the turtle to a specified position (x, y).
color(color): Set the pen color.
"""
