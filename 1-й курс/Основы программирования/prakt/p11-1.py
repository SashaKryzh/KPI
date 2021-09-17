
import datetime as dt

output_file = open('warehouse-output.txt', 'w')

for line in open('warehouse.txt', 'r'):
	item = line.rstrip('\n').split(',')
	combined_price = int(item[1]) * int(item[2])
	stored_time = dt.datetime.now() - dt.datetime.strptime(item[3], '%Y.%m.%d')
	if combined_price > 1000 and stored_time.days > 30:
		string = ' '.join(item)
		output_file.write(string + '\n')
		print(string)

output_file.close()


