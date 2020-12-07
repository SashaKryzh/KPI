
eng2rus = {
	'cat': 'кот',
	'dog': 'собака',
	'car': 'машина',
	'plane': 'самолет',
	'two': 'два',
	'girl': 'девочка',
	'one': 'один',
	'cup': 'чашка',
	'school': 'школа',
	'snake': 'змея'
}

eng2rus.update(dict([reversed(item) for item in eng2rus.items()]))

original = input().lower()
print(eng2rus[original])
