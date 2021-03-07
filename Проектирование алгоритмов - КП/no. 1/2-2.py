import turtle


def polygon(sides, size):
	a = 360 / sides
	for i in range(sides):
		turtle.forward(size)
		turtle.right(a)


def figure(n):
	size = 30
	diff = 10
	initial_sides = 3
	for i in range(n):
		polygon(initial_sides + i, size)
		size += diff

turtle.shape('turtle')

n = int(input())

figure(n)

turtle.exitonclick()
