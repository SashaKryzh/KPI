import turtle


def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


def figure(n):
    size = 20
    diff = 10
    for i in range(n):
        turtle.penup()
        count = i + 1
        turtle.goto(-diff * count, diff * count)
        turtle.pendown()
        square(size)
        size += diff * 2


turtle.shape('turtle')

n = int(input())

figure(n)

turtle.exitonclick()
