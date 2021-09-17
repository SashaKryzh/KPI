
n = int(input())
last = n % 10

if last == 1 and n % 100 != 11:
    word = 'студент'
elif (last in range(2, 5)) and (n % 100 not in range(11, 20)):
    word = 'студента'
elif (last == 0) or (last in range(5, 10)) or (n % 100 in range(11, 20)):
    word = 'студентов'

print('Количество присутствующих: %d %s' % (n, word))

