import turtle
import math


def calc_diagonal(size):
    return math.sqrt(pow(size, 2) * 2)


def figure():
    turtle.left(90)

    # Stamp circle
    turtle.shape("circle")
    turtle.shapesize(0.3, 0.3)
    turtle.stamp()
    turtle.shape("classic")
    turtle.shapesize(1, 1)

    size = 20
    steps = [size, calc_diagonal(size)]
    turns = ['r', 'l', 'l', 'r']

    for i in range(31):
        turtle.forward(steps[i % 2])

        # Select angle
        if i <= 10:
            angle = 45 if i % 2 else 135
            if i % 2:
                size += 20
        elif i <= 19:
            angles = [45, 45, 135, 135]
            angle = angles[i % 4]
        else:
            angles = [45, 135, 45, 135]
            angle = angles[i % 4]
            if i % 2 == False:
                size -= 20

        # Turn
        turn = turns[i % 4]
        turtle.right(angle if turn == 'r' else -angle)

        steps[1] = calc_diagonal(size)

    turtle.right(45)


turtle.speed(0)

figure()

turtle.exitonclick()


