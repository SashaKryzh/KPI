import turtle


def figure():
    turtle.shape("circle")
    turtle.shapesize(0.3, 0.3)
    turtle.stamp()
    turtle.shape("classic")
    turtle.shapesize(1, 1)

    steps = [40, 10]
    for i in range(19):
        index = i % 2
        turtle.forward(steps[index])
        turtle.right(90)
        steps[index] += 10
    turtle.forward(steps[1] - 10)


figure()

turtle.exitonclick()
