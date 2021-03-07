
minutes = int(input()) % 1440

print('{:0>2d}:{:0>2d}'.format(minutes // 60, minutes % 60))

