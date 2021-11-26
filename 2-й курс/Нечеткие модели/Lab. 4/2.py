import itertools
import random
import numpy as np
from math import exp, sqrt
from matplotlib import pyplot as plt

S1 = 3
p = []
t = []
lr = 0.01
for i in itertools.count(start=0.5, step=0.2):
    if i > 4:
        break
    p.append(i)
    t.append(exp(-i))
rab = len(p)

i = 1
c = []
sig = []
while (i <= S1):
    c.append(p[i])
    sig.append(7)
    i = i+1

R = 1
S2 = 1

w = []
for i in range(0, S1):
    arr = random.uniform(8, 10)
    w.append(arr)

err_goal = 0.001
epoch = 0
while 1:
    s = 0
    y = []
    u = np.zeros((rab, S1))
    f = np.zeros((rab, S1))
    for k1 in range(rab):
        e = 0
        for k2 in range(S1):
            rab_e = ((p[k1]-c[k2])**2/(sig[k2]**2))
            u[k1, k2] = u[k1, k2] + rab_e
            f[k1, k2] = exp(-0.5*u[k1, k2])
            e = e+w[k2]*f[k1, k2]
        y.append(e)
        s = s+(e-t[k1])**2
    s = s/rab
    epoch = epoch+1
    if epoch > 10**5:
        break
    de_dc = np.zeros(S1)
    de_dsig = np.zeros(S1)
    de_dw = np.zeros(S1)
    for k2 in range(S1):
        for k1 in range(rab):
            rab_e = y[k1]-t[k1]
            de_dc[k2] = de_dc[k2]+rab_e*w[k2] * \
                exp(-0.5*u[k1, k2])*((p[k1]-c[k2])/(sig[k2]**2))
            de_dsig[k2] = de_dsig[k2]+rab_e*w[k2] * \
                exp(-0.5*u[k1, k2])*((p[k1]-c[k2])**2 / (sig[k2]**3))
            de_dw[k2] = de_dw[k2] + rab_e*exp(-0.5*u[k1, k2])
    for k1 in range(S1):
        c[k1] = c[k1]-lr*de_dc[k1]
        sig[k1] = sig[k1]-lr*de_dsig[k1]
        w[k1] = w[k1]-lr*de_dw[k1]

Y = np.dot(f, w)
E = (Y-t)**2
RES = sum(E)/rab

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(121, polar=False)
ax1.plot(p, t, 'ok')
ax1.plot(p, t, 'b')
ax1.set_title(u'Function')
ax1.set_xlabel(u'x')
ax1.set_ylabel(u't')

ax1.grid(True)
ax2 = fig.add_subplot(122, polar=False)
ax2.plot(p, y, 'sg')
ax2.plot(p, y, 'c')
ax2.set_title(u'Approximation')
ax2.set_xlabel(u'x')
ax2.set_ylabel(u'y')
ax2.grid(True)

p2 = np.linspace(8, 10, 9)
rab = p2.size
yy = np.zeros((S1, rab))
for k1 in range(S1):
    for i in range(rab):
        yy[k1, i] = exp(-0.5*(p2[i]-c[k1])**2/(sig[k1]**2))

T1 = np.zeros(rab)
Y1 = np.dot(np.transpose(w), yy)
for i in range(rab):
    T1[i] = (2*p[i]+1)/sqrt(p[i])

RES1 = sum((Y1-T1)**2)/rab

fig3 = plt.figure(figsize=(15, 15))
ax3 = fig3.add_subplot(211)
for k1 in range(S1):
    ax3.plot(p2[:], yy[k1, :], '-k')

ax3.set_ylabel('mu')
ax3.set_xlabel('Input 1')
ax4 = fig3.add_subplot(212)
ax4.plot(p2, T1, '*k', p2, Y1, 'ok')
ax4.set_title('Approximation - o')
ax4.set_xlabel('Input1')
ax4.set_ylabel('Target - *')
plt.show()