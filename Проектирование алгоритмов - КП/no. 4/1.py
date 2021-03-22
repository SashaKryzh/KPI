
import re

vovewls = 'aeiouyаеёиоуыэюяіїє'
consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфчцчшщґ'


def countLetters(word):
    v, c = 0, 0
    for l in word.lower():
        if l in vovewls:
            v += 1
        elif l in consonants:
            c += 1
    return v, c


file = open('input.txt', mode='r')
text = file.read()
file.close()

words = list(filter(lambda x: x != '', re.split(r'(\s+)', text)))

for w in words[:]:
    if w[0] not in vovewls and w[0] not in consonants:
        continue
    v, c = countLetters(w)
    if c < v:
        words.remove(w)

result = ''.join(words)

print(result)

file = open('output.txt', mode='w')
file.write(result)
file.close()

