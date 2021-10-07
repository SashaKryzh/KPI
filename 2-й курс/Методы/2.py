import sys
import matplotlib.pyplot as plt
import numpy as np

table = []


def calculate(x):
    l = 0
    try:
        for i in range(len(table)):
            g = 1
            for j in range(len(table)):
                if i != j:
                    g = g * ((x - table[j][0])/(table[i][0] - table[j][0]))
            l = l + table[i][1] * g
    except ZeroDivisionError:
        print('Division by zero: Something wrong with your table. The result is false.')
    return l


def enterNewTable():
    global table
    table = []
    print('Enter table values seperated by a new line "X Y"\nTo finish write "end":')
    while True:
        try:
            line = input()
            if line == 'end':
                print()
                break
            else:
                splited = line.split(' ')
                table.append((float(splited[0]), float(splited[1])))
        except:
            print('Wrong input')


def showTable():
    if len(table) == 0:
        print('Table is empty\n')
        return
    xs = 'X:'
    ys = 'Y:'
    for xy in table:
        xs += f'{xy[0]: 10}|'
        ys += f'{xy[1]: 10}|'
    print(f'Table of values of a function:\n{xs}\n{ys}\n')


def enterValue():
    while True:
        print('Enter value X: ', end='')
        try:
            x = float(input())
            Y = calculate(x)
            print(f'Y = {Y}')

            print('Do you want to add this result to the table?\n1 - Yes\n2 - No')
            while True:
                try:
                    s = input()
                    if s == '1':
                        table.append((x, Y))
                        break
                    elif s == '2':
                        break
                except:
                    continue
            return
        except:
            print('Enter number')


def showGraph():
    start = min(table, key=lambda t: t[0])[0] - 0.5
    end = max(table, key=lambda t: t[0])[0] + 0.5
    x = np.arange(start, end + 1, 0.1)
    Y = [calculate(x) for x in x]
    plt.plot(x, Y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


def exit():
    print('Bye! Have a nice day :)')
    sys.exit()


commands = [enterNewTable, showTable, enterValue, showGraph, exit]


def menu():
    print('1 - Enter new table\n2 - Show table\n3 - Enter value\n4 - Show graph\n5 - Exit')
    while True:
        try:
            s = int(input())
            if s >= 1 and s <= len(commands):
                return s - 1
        except:
            continue


if __name__ == "__main__":
    table = [(-1, 1), (0, -8), (1, -3), (3, 25)]
    showTable()
    while True:
        commands[menu()]()
