import numpy as np
import pandas as pd
from collections import Counter

data = pd.DataFrame({
    "Спостереження-сонце": ['+', '+', '-', '-', '-', '-', '-', '+', '+', '-', '+', '-', '-', '-'],
    "Температура-жарко": ['+', '+', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '+', '-'],
    "Дощ": ['-', '-', '-', '+', '+', '+', '-', '-', '-', '+', '-', '-', '-', '+'],
    "Гра": ['-', '-', '+', '-', '-', '-', '+', '-', '+', '-', '+', '+', '+', '-']
})


class CART_classifier():
    def getMinGini(self, data, col, control_col=-1):
        gini = np.inf
        best_k = None
        for k in np.unique(data.iloc[:, col]):
            total_rows = data.shape[0]
            part_data = data[data.iloc[:, col] == k]
            part_rows = part_data.shape[0]
            left_data = data[data.iloc[:, col] != k]
            left_rows = left_data.shape[0]
            new_gini = part_rows / total_rows * self.calc_gini(
                part_data.iloc[:, control_col]) + left_rows / total_rows * self.calc_gini(
                left_data.iloc[:, control_col])
            if new_gini < gini:
                gini = new_gini
                best_k = k
            return gini, k

    def calc_gini(self, col):
        total = col.size
        pos = (col == '+').sum()
        neg = total - pos
        return 1 - (pos / total) ** 2 - (neg / total) ** 2

    def buildTree(self, data, level=1):
        cols = data.shape[1]
        tree_ginis = np.zeros((cols - 1, 2))

        for i in range(cols - 1):
            tree_ginis[i, 0] = i
            gini, val = self.getMinGini(data, i, cols - 1)
            tree_ginis[i, 1] = gini
        min_gini_idx = np.argmin(tree_ginis[:, 1])

        for k in np.unique(data.iloc[:, min_gini_idx]):
            new_data = data[data.iloc[:, min_gini_idx] == k]
            new_data = new_data.drop(new_data.columns[min_gini_idx], axis=1)
            l = '--' * level
            print(l + ' ' + data.columns[min_gini_idx] + ': ' + k)

            if self.calc_gini(new_data.iloc[:, -1]) == 0:
                print('--' * (level + 1) + ' ' + 'Рішення: ' + new_data.iloc[0, -1])
            else:
                self.buildTree(new_data, level + 1)

model = CART_classifier()
print('Гра')
model.buildTree(data)
