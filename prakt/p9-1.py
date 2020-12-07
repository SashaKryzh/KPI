
import re
import itertools

vowels = 'aeiou' + 'аеиіоуяюєї' + 'аоиеёэыуюя'
vowels = vowels + vowels.upper()

s = input('Input text: ')

splited = re.split(r'[.!?]', s)
striped = list(map(str.strip, splited))
no_empty = list(filter(lambda x: x != '', striped))

if not no_empty:
	print('You should input at least 1 sentence')
	exit()

print('a:')
for sentence in no_empty:
	words = len(sentence.split())
	print('{} words in "{}"'.format(words, sentence))

print('b:')
print('The longest sencence is: "{}"'.format(max(no_empty, key=len)))

print('c:')
words = list(itertools.chain.from_iterable(map(str.split, splited)))
words = list(filter(lambda x: x[-2] not in vowels if len(x) > 1 else x, words))
print(words)

