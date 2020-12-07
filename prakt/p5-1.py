
import numpy as np

x0 = 1.76
xk = -2.5
dx = -0.25

b = 35.4

x = x0

while np.arange(x0, xk, dx):
	y = 10**-3 * x**(5 / 2) + x + b
	print('x =', round(x, 2), 'y =', y)
	x += dx



