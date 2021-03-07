import turtle
import math


def calc_diagonal(size):
	return math.sqrt(pow(size, 2) * 2)


def figure():
	turtle.shape("circle")
	turtle.shapesize(0.3, 0.3)
	turtle.stamp()
	turtle.shape("classic")
	turtle.shapesize(1, 1)

	turtle.left(90)

	size = 20
	steps = [size, calc_diagonal(size)]
	turns = ['r', 'l', 'l', 'r']

	for i in range(40):
		turtle.forward(steps[i % 2])

		if i <= 10 or i >= 17:
			angle = 45 if (i % 2) else 135
			if i % 2:
				size += 20
		else:
			angle = 45 if (i % 2) else 135

		turn = turns[i % 4]
		turtle.right(angle if turn == 'r' else -angle)        
		
		steps[1] = calc_diagonal(size)


turtle.speed(0)

figure()

turtle.exitonclick()
