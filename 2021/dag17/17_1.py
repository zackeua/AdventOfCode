import sys
from math import sqrt

with open(sys.argv[1], 'r') as f:
    data = f.readline()
    data = data.split(': ')
    data = data[1]
    data = data.split(', ')
    x = data[0]
    y = data[1]
    x = x.split('=')[1]
    y = y.split('=')[1]

    x_min, x_max = list(map(int, x.split('..')))
    y_min, y_max = list(map(int, y.split('..')))
    #print(x_min, x_max)
    #print(y_min, y_max)


x_vel_min = int(-1/2 + sqrt(2 * x_min + 1/4))
x_vel_max = int(-1/2 + sqrt(2 * x_max + 1/4))+1
#print(x_vel_min, x_vel_max)

y_vel_init = -y_min
best = 0
x_vel_init = x_vel_min+1
while y_vel_init != 0:
    x_pos = 0
    y_pos = 0
    y_vel = y_vel_init
    x_vel = x_vel_init
    temp_best = 0
    while y_pos >= y_min:
        x_pos += x_vel
        y_pos += y_vel
        if y_pos > temp_best:
            temp_best = y_pos
        if x_vel > 0: x_vel -= 1
        y_vel -= 1
        print(x_pos, y_pos)
        if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
            if best < temp_best:
                best = temp_best
    y_vel_init -= 1

print(best)
