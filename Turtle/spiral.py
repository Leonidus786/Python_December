import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

for i in range(36):
    my_turtle.forward(i * 10)
    my_turtle.right(20)

screen.exitonclick()
