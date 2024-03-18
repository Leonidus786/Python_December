import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)

screen.exitonclick()
