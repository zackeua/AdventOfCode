import sys
def show(grid):
    zlim1 = 0
    zlim2 = 0
    ylim1 = 0
    ylim2 = 0
    xlim1 = 0
    xlim2 = 0

    while (zlim1,0,0) in grid:
        zlim1 -= 1
    while (zlim2,0,0) in grid:
        zlim2 += 1
    while (0,ylim1,0) in grid:
        ylim1 -=1
    while (0,ylim2,0) in grid:
        ylim2 +=1
    while (0,0,xlim1) in grid:
        xlim1 -=1
    while (0,0,xlim2) in grid:
        xlim2 +=1
    for z in range(zlim1+1, zlim2):
        print(f'z={z}')
        for x in range(xlim1+1, xlim2):
            for y in range(ylim1+1, ylim2):
                print('#' if grid[(z,y,x)] else '.',end="")
            print()
        print()


with open(sys.argv[1], 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = data[:-1]
    print(data)

d = {}
t = {}

w_min = 0
w_max = 0

z_min = 0
z_max = 0

y_min = 0
y_max = len(data)

x_min = 0
x_max = len(data[0])
for w in range(w_min, w_max + 1):
    for z in range(z_min, z_max + 1):
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                if data[x][y] == ".":
                    d[(w,z,y,x)] = 0
                    t[(w,z,y,x)] = 0
                else:
                    d[(w,z,y,x)] = 1
                    t[(w,z,y,x)] = 1

c = 0
while c < 6:
    print(c)
    #show(d)

    for w in range(w_min-2, w_max+3):
        for z in range(z_min-2, z_max+3):
            for y in range(y_min-2, y_max+2):
                for x in range(x_min-2, x_max+2):
                    if not (w,z,y,x) in d:
                        d[(w,z,y,x)] = 0
                        t[(w,z,y,x)] = 0

    for w in range(w_min-1, w_max + 2):
        for z in range(z_min-1, z_max + 2):
            for y in range(y_min-1, y_max+1):
                for x in range(x_min-1, x_max+1):
                    sum = 0

                    sum += d[(w-1,z-1,y-1,x-1)] == 1
                    sum += d[(w-1,z-1,y-1,x)] == 1
                    sum += d[(w-1,z-1,y-1,x+1)] == 1
                    sum += d[(w-1,z-1,y,x-1)] == 1
                    sum += d[(w-1,z-1,y,x)] == 1
                    sum += d[(w-1,z-1,y,x+1)] == 1
                    sum += d[(w-1,z-1,y+1,x-1)] == 1
                    sum += d[(w-1,z-1,y+1,x)] == 1
                    sum += d[(w-1,z-1,y+1,x+1)] == 1

                    sum += d[(w-1,z,y-1,x-1)] == 1
                    sum += d[(w-1,z,y-1,x)] == 1
                    sum += d[(w-1,z,y-1,x+1)] == 1
                    sum += d[(w-1,z,y,x-1)] == 1
                    sum += d[(w-1,z,y,x)] == 1
                    sum += d[(w-1,z,y,x+1)] == 1
                    sum += d[(w-1,z,y+1,x-1)] == 1
                    sum += d[(w-1,z,y+1,x)] == 1
                    sum += d[(w-1,z,y+1,x+1)] == 1

                    sum += d[(w-1,z+1,y-1,x-1)] == 1
                    sum += d[(w-1,z+1,y-1,x)] == 1
                    sum += d[(w-1,z+1,y-1,x+1)] == 1
                    sum += d[(w-1,z+1,y,x-1)] == 1
                    sum += d[(w-1,z+1,y,x)] == 1
                    sum += d[(w-1,z+1,y,x+1)] == 1
                    sum += d[(w-1,z+1,y+1,x-1)] == 1
                    sum += d[(w-1,z+1,y+1,x)] == 1
                    sum += d[(w-1,z+1,y+1,x+1)] == 1


                    sum += d[(w,z-1,y-1,x-1)] == 1
                    sum += d[(w,z-1,y-1,x)] == 1
                    sum += d[(w,z-1,y-1,x+1)] == 1
                    sum += d[(w,z-1,y,x-1)] == 1
                    sum += d[(w,z-1,y,x)] == 1
                    sum += d[(w,z-1,y,x+1)] == 1
                    sum += d[(w,z-1,y+1,x-1)] == 1
                    sum += d[(w,z-1,y+1,x)] == 1
                    sum += d[(w,z-1,y+1,x+1)] == 1

                    sum += d[(w,z,y-1,x-1)] == 1
                    sum += d[(w,z,y-1,x)] == 1
                    sum += d[(w,z,y-1,x+1)] == 1
                    sum += d[(w,z,y,x-1)] == 1
                    #sum += d[(w,z,y,x)] == 1
                    sum += d[(w,z,y,x+1)] == 1
                    sum += d[(w,z,y+1,x-1)] == 1
                    sum += d[(w,z,y+1,x)] == 1
                    sum += d[(w,z,y+1,x+1)] == 1

                    sum += d[(w,z+1,y-1,x-1)] == 1
                    sum += d[(w,z+1,y-1,x)] == 1
                    sum += d[(w,z+1,y-1,x+1)] == 1
                    sum += d[(w,z+1,y,x-1)] == 1
                    sum += d[(w,z+1,y,x)] == 1
                    sum += d[(w,z+1,y,x+1)] == 1
                    sum += d[(w,z+1,y+1,x-1)] == 1
                    sum += d[(w,z+1,y+1,x)] == 1
                    sum += d[(w,z+1,y+1,x+1)] == 1

                    sum += d[(w+1,z-1,y-1,x-1)] == 1
                    sum += d[(w+1,z-1,y-1,x)] == 1
                    sum += d[(w+1,z-1,y-1,x+1)] == 1
                    sum += d[(w+1,z-1,y,x-1)] == 1
                    sum += d[(w+1,z-1,y,x)] == 1
                    sum += d[(w+1,z-1,y,x+1)] == 1
                    sum += d[(w+1,z-1,y+1,x-1)] == 1
                    sum += d[(w+1,z-1,y+1,x)] == 1
                    sum += d[(w+1,z-1,y+1,x+1)] == 1

                    sum += d[(w+1,z,y-1,x-1)] == 1
                    sum += d[(w+1,z,y-1,x)] == 1
                    sum += d[(w+1,z,y-1,x+1)] == 1
                    sum += d[(w+1,z,y,x-1)] == 1
                    sum += d[(w+1,z,y,x)] == 1
                    sum += d[(w+1,z,y,x+1)] == 1
                    sum += d[(w+1,z,y+1,x-1)] == 1
                    sum += d[(w+1,z,y+1,x)] == 1
                    sum += d[(w+1,z,y+1,x+1)] == 1

                    sum += d[(w+1,z+1,y-1,x-1)] == 1
                    sum += d[(w+1,z+1,y-1,x)] == 1
                    sum += d[(w+1,z+1,y-1,x+1)] == 1
                    sum += d[(w+1,z+1,y,x-1)] == 1
                    sum += d[(w+1,z+1,y,x)] == 1
                    sum += d[(w+1,z+1,y,x+1)] == 1
                    sum += d[(w+1,z+1,y+1,x-1)] == 1
                    sum += d[(w+1,z+1,y+1,x)] == 1
                    sum += d[(w+1,z+1,y+1,x+1)] == 1


                    if d[(w,z,y,x)] == 1:
                        if 2 <= sum <= 3:
                            t[(w,z,y,x)] = 1
                        else:
                            t[(w,z,y,x)] = 0
                    else:
                        if sum == 3:
                            t[(w,z,y,x)] = 1
                        else:
                            t[(w,z,y,x)] = 0


    for w in range(w_min-1, w_max + 2):
        for z in range(z_min-1, z_max + 2):
            for y in range(y_min-1, y_max+1):
                for x in range(x_min-1, x_max+1):
                    d[(w,z,y,x)] = t[(w,z,y,x)]


    w_min -= 1
    w_max += 1

    z_min -= 1
    z_max += 1

    y_min -= 1
    y_max += 1

    x_min -= 1
    x_max += 1

    c += 1

total = 0
for w in range(w_min, w_max + 1):
    for z in range(z_min, z_max + 1):
        for y in range(y_min, y_max):
            for x in range(x_min, x_max):
                total += d[(w,z,y,x)] == 1

print(total)
