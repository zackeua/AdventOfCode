import sys

def sign(x):
    return abs(x)//x

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

y_vel_init = -y_min
pos = []
while y_vel_init >= y_min:
    x_vel_init = x_max
    while x_vel_init != 0:
        x_pos = 0
        y_pos = 0
        y_vel = y_vel_init
        x_vel = x_vel_init

        while y_pos >= y_min:
            x_pos += x_vel
            y_pos += y_vel
            if x_vel != 0: x_vel -= 1# sign(x_vel)
            y_vel -= 1
            if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
                if (x_vel_init, y_vel_init) not in pos:
                    pos.append((x_vel_init, y_vel_init))
        
        x_vel_init -= 1
    y_vel_init -= 1

print(len(pos))