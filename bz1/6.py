
s1 = int(input())
e1 = int(input())
s2 = int(input())
e2 = int(input())

if s1 > e1:
	s1, e1 = e1, s1
if s2 > e2:
	s2, e2 = e2, s2

i = 0
count = 0

while i <= 100:
	count += (s1 <= i <= e1) and (s2 <= i <= e2)
	i += 1

print(count)

