import turtle


def circles(radius):
	turtle.circle(-radius)
	turtle.circle(radius)


def figure(n):
	turtle.left(90)
	radius = 30
	diff = 5
	for i in range(n):
		circles(radius)
		radius += diff


turtle.shape('turtle')

n = int(input())

figure(n)

turtle.exitonclick()
