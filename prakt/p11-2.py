
import re

f = open('input.txt', 'r')
lines = f.readlines()
f.close()

words = []
for i, line in enumerate(lines):
	lines[i] = list(filter(lambda x: x != '', re.split(r'[\s.,;!?-]', line)))
	words += list(map(lambda x: x.lower(), lines[i]))

removed = []
for line in lines:
	for word in line[:]:
		if words.count(word.lower()) > 1:
			line.remove(word)
			removed.append(word)

print('Видалені слова: {}'.format(', '.join(removed)))

f = open('output.txt', 'w')
for line in lines:
	f.write(' '.join(line) + '\n')
f.close()


