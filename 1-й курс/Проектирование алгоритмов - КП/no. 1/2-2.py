import turtle


def polygon(sides, size):
    a = 360 / sides
    for i in range(sides):
        turtle.forward(size)
        turtle.left(a)


def figure(n):
    size = 30
    z = 10

    for i in range(3, 3 + n):
        angle = 180 * (i - 2) / i

        turtle.left(180 - (angle / 2))

        polygon(i, size)

        turtle.right(180 - (angle / 2))

        turtle.penup()
        turtle.goto(turtle.xcor() + z, turtle.ycor())
        z += 3
        turtle.pendown()

        size += 10


turtle.speed(0)
turtle.shape('turtle')

n = int(input())

figure(n)

turtle.exitonclick()
