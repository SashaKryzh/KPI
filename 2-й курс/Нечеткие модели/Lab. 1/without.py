import matplotlib.pyplot as plt
import numpy as np


def zFunc(x, a, b):
    if (x <= a):
        return 1
    elif (a <= x and x <= (a + b) / 2):
        return 1 - 2 * (((x - a) / (b - a))**2)
    elif ((a + b) / 2 <= x and x <= b):
        return 2 * (((x - b) / (b - a))**2)
    elif (x >= b):
        return 0


def sFunc(x, a, b):
    return 1 - zFunc(x, a, b)


def pFunc(x, a, b, c, d):
    if (x <= a):
        return 0
    elif (a <= x and x <= b):
        return sFunc(x, a, b)
    elif (b <= x and x <= c):
        return 1
    elif (c <= x and x <= d):
        return zFunc(x, c, d)
    elif (x >= d):
        return 0


X = np.arange(60, 220)

fig, ax = plt.subplots()

ax.set_xlabel("Тиск")
ax.set_ylabel("Належність")
ax.set_title("Без використання бібліотеки skfuzzy")

ax.plot(X, [zFunc(x, 80, 100) for x in X], label="Низький")
ax.plot(X, [pFunc(x, 100, 115, 125, 140) for x in X], label="Помірний")
ax.plot(X, [sFunc(x, 140, 160) for x in X], label="Високий")

ax.plot(X, [1 - zFunc(x, 80, 100)**2 for x in X], label="Не дуже низький")
ax.plot(X, [pFunc(x, 100, 115, 125, 140)**(1/2)
        for x in X], label="Більш-менш помірний")
ax.plot(X, [sFunc(x, 140, 160)**2 for x in X], label="Дуже високий")

ax.legend()

plt.grid()
plt.show()
