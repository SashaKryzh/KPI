import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = [0.2, 0.8]
A = np.linspace(0, 1, 100)
B = np.linspace(0, 1, 100)

vert0 = A.copy()
vert1 = A.copy()
for i in range(len(vert0)):
    vert0[i] = x[0]
    vert1[i] = x[1]

A11 = fuzz.trimf(A, [0, 0, 1])
A12 = fuzz.trimf(A, [0, 1, 1])
B1 = fuzz.trimf(A, [0, 0, 1])
B2 = fuzz.trimf(A, [0, 1, 1])

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
ax0.set_xlim([0, 1])
ax0.set_ylim([0, 1])
ax1.set_xlim([0, 1])
ax1.set_ylim([0, 1])
ax2.set_xlim([0, 1])
ax2.set_ylim([0, 1])

ax0.plot(vert0, A11, 'y', linewidth=1.5, label='X1')
ax0.plot(A, A11, 'b', linewidth=1.5, label='A11')
ax0.plot(A, A12, 'g', linewidth=1.5, label='A12')
ax0.set_title('A1')
ax0.legend()
ax1.plot(vert1, A11, 'y', linewidth=1.5, label='X2')
ax1.plot(A, A11, 'b', linewidth=1.5, label='A21')
ax1.plot(A, A12, 'g', linewidth=1.5, label='A22')
ax1.set_title('A2')
ax1.legend()

ax2.plot(B, B1, 'b', linewidth=1.5, label='B1')
ax2.plot(B, B2, 'g', linewidth=1.5, label='B2')
ax2.set_title('B')
ax2.legend()


for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

a11_level = fuzz.interp_membership(A, A11, x[0])
a12_level = fuzz.interp_membership(A, A12, x[0])
a21_level = fuzz.interp_membership(A, A11, x[1])
a22_level = fuzz.interp_membership(A, A12, x[1])

rulelist = [[0, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
            [1, 1, 1]]

alpha = [0, 0, 0, 0]
for i in range(4):
    if rulelist[i][0] == 0:
        v_1 = a11_level
    else:
        v_1 = a12_level
    if rulelist[i][1] == 0:
        v_2 = a21_level
    else:
        v_2 = a22_level
    alpha[i] = np.multiply(v_1, v_2)

B_all = np.zeros([4, len(B)])
for i in range(len(alpha)):
    if rulelist[i][2] == 0:
        for j in range(len(B_all[i])):
            B_all[i][j] = (1-B[j])*alpha[i]
    if rulelist[i][2] == 1:
        for j in range(len(B_all[i])):
            B_all[i][j] = B[j]*alpha[i]

res1 = np.maximum(B_all[0], B_all[1])
res2 = np.maximum(B_all[2], B_all[3])
res = np.maximum(res1, res2)

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
ax0.set_xlim([0, 1])
ax0.set_ylim([0, 1])
ax1.set_xlim([0, 1])
ax1.set_ylim([0, 1])
ax2.set_xlim([0, 1])
ax2.set_ylim([0, 1])
ax0.plot(B, B_all[1], 'b', linewidth=1.5, label='B1')
ax0.fill_between(B, 0, B_all[1], alpha=0.30)
ax1.plot(B, B_all[2], 'g', linewidth=1.5, label='B2')
ax1.fill_between(B, 0, B_all[2], alpha=0.30, facecolor='green')
ax2.plot(B, res, 'g', linewidth=1.5, label='Res')
ax2.fill_between(B, 0, res, alpha=0.30, facecolor='green')
ax0.legend()
ax1.legend()
ax2.legend()
plt.show()

print("Compare methods:")
for method in ['centroid',
               'bisector',]:
    y = fuzz.defuzz(B, res, method)
    print("y_({}) = ".format(method), y)
