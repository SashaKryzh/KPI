

def func(a1, a2, b1, b2):
	a1, a2, b1, b2 = list(a1), list(a2), list(b1), list(b2)

	# Stabilize X
	if a1[0] > a2[0]:
		a1, a2 = a2, a1
	if b1[0] > b2[0]:
		b1, b2 = b2, b1

	# Stabilize Y
	if a1[1] > a2[1]:
		a1[1], a2[1] = a2[1], a1[1]
	if b1[1] > b2[1]:
		b1[1], b2[1] = b2[1], b1[1]

	area1 = abs(a1[0] - a2[0]) * abs(a1[1] - a2[1])
	area2 = abs(b1[0] - b2[0]) * abs(b1[1] - b2[1])

	# Intersect area
	x_dist = min(a2[0], b2[0]) - max(a1[0], b1[0])
	y_dist = min(a2[1], b2[1]) - max(a1[1], b1[1])

	areaI = 0
	if x_dist > 0 and y_dist > 0:
		areaI = x_dist * y_dist

	return area1 + area2 - areaI


print(func((0, 2), (5, 6), (3, 3), (7, 0)))
print(func((5, 7), (2, 2), (3, 4), (6, 9)))
