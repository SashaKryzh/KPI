import datetime as dt


string = input()

try:
    date = dt.datetime.strptime(string, '%m/%d/%Y')
except:
	try:
		date = dt.datetime.strptime(string, '%B %d %Y')
	except:
		raise Exception('Wrong input')

print(date.strftime('%d/%m/%Y'))
