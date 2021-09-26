import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

X = np.arange(60, 220)

fig, ax = plt.subplots()

ax.set_xlabel("Тиск")
ax.set_ylabel("Належність")
ax.set_title("З використанням бібліотеки skfuzzy")

ax.plot(X, fuzz.zmf(X, 80, 100), label="Низький")
ax.plot(X, fuzz.pimf(X, 100, 115, 125, 140), label="Помірний")
ax.plot(X, fuzz.smf(X, 140, 160), label="Високий")

ax.plot(X, 1 - fuzz.zmf(X, 80, 100)**2, label="Не дуже низький")
ax.plot(X, fuzz.pimf(X, 100, 115, 125, 140)
        ** (1/2), label="Більш-менш помірний")
ax.plot(X, fuzz.smf(X, 140, 160)**2, label="Дуже високий")


ax.legend()

plt.grid()
plt.show()
