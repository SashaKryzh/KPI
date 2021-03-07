import turtle


def classic_shape(t):
    t.shape("classic")
    t.shapesize(1, 1)


def stamp_circle(t):
    t.shape("circle")
    t.shapesize(0.3, 0.3)
    t.stamp()


def figure():
    t1 = turtle.Turtle()
    t1.speed(0)
    t2 = turtle.Turtle()
    t2.speed(0)

    steps = [90, 15]

    stamp_circle(t1)
    t1.right(90)
    classic_shape(t1)

    t2.penup()
    t2.setpos(steps[1], -steps[0])
    t2.pendown()
    t2.left(90)
    stamp_circle(t2)
    classic_shape(t2)

    steps_to_take = 4

    for i in range(steps_to_take):
        for j in range(2):
            t = t1 if j == 0 else t2
            t.forward(steps[0])
            t.right(90)
            t.forward(steps[1])
            t.right(90)
            t.forward(steps[0])

            if i == steps_to_take - 1:
                continue

            t.left(90)
            t.forward(steps[1])
            t.left(90)


figure()

turtle.exitonclick()
