from random import randint


'''
	Щоб максимально легко виграти в цю гру, потрібно почати з середнього чила (у нас це 50).
	Потім на кожному кроці змінювати число на *половину вгору чи в низ. Наприклад:
		50 -> 75 -> 63 -> 69 -> 66
		   +     -     +     -
	І продовжувати доки не вгадаєте число :)
'''


def check_num(guess):
    if guess == x:
        return 'GOOD'
    return 'LOWER' if x < guess else 'GREATER'


x = randint(1, 100)

for i in range(10):
    guess = int(input('Enter your guess: '))
    result = check_num(guess)
    if result == 'GOOD':
        print('You win! ({})'.format(i + 1))
        break
    else:
        print(result)
    print('---')
else:
    print('You lose :(')
