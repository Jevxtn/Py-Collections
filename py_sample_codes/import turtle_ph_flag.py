import turtle

# Set up the turtle
flag = turtle.Turtle()
flag.speed(0)
flag.penup()
flag.goto(-200, 100)
flag.pendown()

# Draw the flag
flag.color("blue")
flag.begin_fill()
for i in range(2):
    flag.forward(400)
    flag.right(90)
    flag.forward(267)
    flag.right(90)
    flag.end_fill()

flag.left(90)
flag.forward(267)
flag.left(90)
flag.forward(200)
flag.color("yellow")
flag.begin_fill()
flag.circle(-50)
flag.end_fill()

flag.penup()
flag.goto(0, 0)
flag.pendown()
flag.color("white")
flag.pensize(10)
for i in range(5):
    flag.forward(180)
    flag.backward(180)
    flag.right(72)

# Hide the turtle
flag.hideturtle()

# Keep the window open
turtle.done()