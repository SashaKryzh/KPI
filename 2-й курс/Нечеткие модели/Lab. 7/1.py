import math
import numpy as np
import matplotlib.pyplot as plt


def distance(w1, w2):
    r = 0
    for i in range(0, w1.size):
        r += (w1[i] - w2[i]) ** 2
    return math.sqrt(r)


with open('data.txt', 'r') as f:
    strings = f.readlines()[200:240]
    startX = []
    i = 0
    for line in strings:
        if (i == (len(strings) - 1)):
            startX.append([float(i) for i in line[:].split(',')])
        else:
            startX.append([float(i) for i in line[:-1].split(',')])
        i += 1

X = np.array(startX)
N = 2;
K = len(X);
L = len(X[0])
U = np.random.rand(N, K)
s = []
for i in range(K):
    s.append(np.sum(U[:, i]))

normator = s
for i in range(len(normator)):
    U[0, i] = U[0, i] / normator[i];
    U[1, i] = U[1, i] / normator[i]
U = U.transpose()
X = np.array(X)
n = K; k = L; c = N;
ite = 50; count = 0
V = np.zeros((c, k)); D = np.zeros((n, c))
count = 0
while count < ite:
    for j in range(1, c):
        for l in range(1, k):
            t1 = 0.0; t2 = 0.0
            for i in range(1, n):
                t1 = t1 + U[i, j] * U[i, j] * X[i, l]
                t2 = t2 + U[i, j] * U[i, j]
            V[j, l] = t1 / t2
    for i in range(1, n):
        for j in range(1, c):
            D[i, j] = distance(X[i, :], V[j, :])
    for i in range(1, c):
        for j in range(1, c):
            t3 = 0.0
            if D[i, j] == 0:
                U[i, j] = 1.0
            else:
                for p in range(1, c):
                    t3 = t3 + (D[i, j] ** 2) / (D[i, p] ** 2)
            U[i, j] = 1.0 / t3
    count = count + 1;
groups = []
for i in range(len(X)):
    maxs = max(U[i])
    for j in range(3):
        if U[i][j] == maxs:
            groups.append(j);
            break
markers = ['o', 'x']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c='b', marker=markers[groups[i]])
fig.show();
plt.show()