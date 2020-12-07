
import random

types = ['passenger car', 'truck']

n = 10
cars = []

for i in range(n):
	cars.append({'type': random.choice(types), 'price': random.randint(1000, 10000)})

print('All cars: {}'.format(cars))

p_car_prices = [car['price'] for car in cars if car['type'] == 'passenger car']
print('Average passenger car price is {}'.format(round(sum(p_car_prices) / len(p_car_prices))))

