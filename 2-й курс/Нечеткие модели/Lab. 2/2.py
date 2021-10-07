import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt


class Model:
    t = []
    y = []
    B = []
    A_1 = []
    A_2 = []

    x = []
    fx = []
    alp = []
    B_i = []
    B_ = []

    res = 0

    def __init__(self, t, y, A1, A2):
        self.t = t
        self.y = np.arange(y[0], y[1], y[2])
        self.B = np.array([1-self.y, self.y])
        self.A_1 = np.arange(A1[0], A1[1], A1[2])
        self.A_2 = np.arange(A2[0], A2[1], A2[2])

    def start(self, x, dezz='centroid'):
        self.x = x
        self.fx = [round(1-x[0], 5), x[0], round(1-x[1], 5), x[1]]

        self.alp = [min(self.fx[int(i//2)], self.fx[2 + i % 2])
                    for i in range(4)]

        for i in range(4):
            self.B_i.append([])
            for j in range(len(self.B[0])):
                self.B_i[i].append(
                    round(min(self.alp[i], self.B[self.t[i]][j]), 3))

        self.B_ = np.array([max([self.B_i[i][j] for i in range(4)])
                            for j in range(len(self.B_i[0]))])

        self.res = fuzzy.defuzz(self.y, self.B_, dezz)
        return self.res

    def print_all(self):
        print("\nБАЗА ПРАВИЛ:")  # База правил
        s = ['R_' + str(i) + ' : if x_1 = A_1' + str(int(i/3)+1) + ' and '
             + 'x_2 = A_2' + str(int(i/3)+1) + ' then y = B_' + str(self.t[i-1]+1) for i in range(1, 5)]
        for i in range(len(s)):
            print(s[i])
        print("\n\nФазифікація:")  # Фазифікація
        print('A_11 = ', '1, ' + str(self.fx[0]) + ' ,0')
        print(
            'A_12 = ', '0, ' + str(self.fx[1]) + ', 1\n')
        print('A_11 = ', '1, ' + str(self.fx[2]) + ' ,0')
        print(
            'A_12 = ', '0, ' + str(self.fx[3]) + ', 1\n')
        print('y = ', self.y)
        print('B1 = ', self.B[0])
        print('B2 = ', self.B[1])
        print("\n\nАктивізація:")  # Активізація
        for i in range(4):
            print('alp_' + str(i) + ' = ', self.alp[i])
            print('B*_' + str(i) + ' = ', self.B_i[i])
        print("\n\nВихід:")  # Вихід
        print('y = ', self.y)
        print('B* = ', self.B_)

    def plot(self):
        for i in range(1, 3):
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 0.5, 0.5])
            ax.plot(self.A_1, self.A_1, label="mA_"+str(i)+"2(P"+str(i)+")")
            ax.plot(self.A_1, self.A_2, label="mA_"+str(i)+"1(P"+str(i)+")")
            ax.plot([self.x[i-1]]*10, np.linspace(0, 1, 10),
                    label="x_" + str(i))
            ax.set_xlim([-0.1, 1.1])
            ax.set_xlabel("P"+str(i)+"")
            ax.set_ylabel("m(P"+str(i)+")")
            ax.set_title("x_"+str(i)+"")
            ax.legend()
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 0.5])
        ax.plot(self.A_1, self.A_1, label="mB_2(y)")
        ax.plot(self.A_1, self.A_2, label="mB_1(y)")
        ax.set_xlabel("y")
        ax.set_ylabel("m(y)")
        ax.set_title("y")
        ax.legend()
        for i in range(1, 5):
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 0.8, 0.5])
            ax.plot(self.B[self.t[i-1]], self.B_i[i-1])
            ax.set_xlim([self.B[self.t[i-1]][0],
                         self.B[self.t[i-1]][len(self.B[0])-1]])
            ax.set_ylim([0, 1.1])
            ax.fill_between(self.B[self.t[i-1]], 0,
                            self.B_i[i-1], alpha=0.30, facecolor='blue')
            ax.set_title("B*_" + str(i))

        fig = plt.figure()
        ax = fig.add_axes([0, 0, 0.8, 0.5])
        ax.plot(self.y, self.B_)
        ax.fill_between(self.y, 0, self.B_, alpha=0.30, facecolor='red')
        ax.set_ylim([0, 1.1])
        ax.set_title("B*")


m = Model([1, 0, 1, 1], [0, 1.1, 0.2], [0, 1.1, 0.1], [1, -0.1, -0.1])
print('Відповідь: ', m.start([0.2, 0.8]))
m.print_all()
m.plot()
