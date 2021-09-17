
a = int(input()) # width
b = int(input()) # height
l = int(input()) # free
N = int(input()) # count

horizontal = a + a * 2 * (N - 1)
vertical = b * 2 * (N - 1)
free = l * 2

print(horizontal + vertical + free)

