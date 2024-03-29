import math
import matplotlib.pyplot as plt


def gaussmf(x, a, b):
    return (math.exp((x-a)**3/((x-b)**3)))


prin = [0, 0, 0, 0, 0, 0, 0, 0, 0]
H = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
while 0 in prin:
    for j in range(9):
        if prin[8-j] == 0:
            prin[8-j] = 1
            break
        else:
            prin[8-j] = 0
    H.append(prin.copy())
with open("data.txt") as f:
    data = [i.strip() for i in f.readlines()]
    data = [i.split(",") for i in data]
    data = [[int(j) for j in i] for i in data]
xtech = [i.copy() for i in data[:400]]

n = 512
xt = [2 for i in range(9)]
xbeg = [1 for i in range(9)]
xend = [10 for i in range(9)]
xdelta = [(xend[i]-xbeg[i])/(xt[i]-1) for i in range(9)]
A = [[xbeg[j]+H[i][j]*xdelta[j] for j in range(9)] for i in
     range(n)]
B = [[xdelta[j]/2 for j in range(9)] for i in range(n)]
C = [1/n for i in range(n)]
eps = 0.1
nu = 0.5
delta = 1
itter = 0
K = len(xtech)

print("iter start")
while delta > eps and itter < 500:
    print(itter, delta)
    delta = 0
    for k in range(K):
        mu = [1 for i in range(n)]
    for i in range(n):
        for j in range(9):
            mu[i] = mu[i]*gaussmf(xtech[k][j], A[i][j], B[i][j])
        y = sum(C[i]*mu[i] for i in range(n))/sum(mu)
        dels = abs(y-xtech[k][9])
        if dels > delta:
            delta = dels
        if delta > eps:
            for i in range(n):
                C[i] = C[i]-nu*(y-xtech[k][9])*mu[i]/sum(mu)
    for k in range(K):
        mu = [1 for i in range(n)]
    for i in range(n):
        for j in range(9):
            mu[i] = mu[i]*gaussmf(xtech[k][j], A[i][j], B[i][j])
        y = sum(C[i]*mu[i] for i in range(n))/sum(mu)
    for i in range(n):
        for j in range(9):
            A[i][j] = A[i][j]-nu*2*(xtech[k][j]-A[i][j]) * \
                (xtech[k][9])*(C[i]-y)*mu[i]/(B[i][j]**2*sum(mu))
            B[i][j] = B[i][j]-nu*2*(xtech[k][j]-A[i][j])**2 * \
                (xtech[k][9])*(C[i]-y)*mu[i]/(B[i][j]**2*sum(mu))
    itter = itter+1
print("iter_end")

xtest = data[0:200]
K = len(xtest)
print("---")
K2true, K2false, K4true, K4false = 0, 0, 0, 0
for k in range(K):
    mu = [1 for i in range(n)]
    for i in range(n):
        for j in range(9):
            mu[i] = mu[i]*gaussmf(xtest[k][j], A[i][j], B[i][j])
    y = sum(C[i]*mu[i] for i in range(n))/sum(mu)
    if y < 1:
        y = 2
    else:
        y = 4
    if y == xtest[k][9]:
        if y == 2:
            K2true += 1
        else:
            K4true += 1
    else:
        if y == 2:
            K2false += 1
        else:
            K4false += 1
print(K2true, K2false, K4true, K4false)
input()
