import sys

class Cube:

    def __init__(self, add, coord):
        self.add = add
        self.left = coord[0][0]
        self.right = coord[0][1]
        self.front = coord[1][0]
        self.back = coord[1][1]
        self.bottom = coord[2][0]
        self.top = coord[2][1]
    
    def volume(self):
        return self.add * (self.right+1 - self.left) * (self.top+1 - self.bottom) * (self.back+1 - self.front)


    def intersect(self, other):
        if self.right < other.left and self.left < other.left \
        or self.left > other.left and self.left > other.right \
        or self.back < other.front and self.back < other.back \
        or self.front > other.back and self.front > other.front \
        or self.top < other.bottom and self.top < other.top \
        or self.bottom > other.top and self.bottom > other.bottom : return None

        if self.add == 1 and other.add == 1:
            add = -1
        elif self.add == 1 and other.add == 0:
            add = -1
        elif self.add == 1 and other.add == -1:
            pass # impossible
        elif self.add == 0 and other.add == 1:
            add = 0
        elif self.add == 0 and other.add == 0:
            add = 0
        elif self.add == 0 and other.add == -1:
            pass # impossible
        elif self.add == -1 and other.add == 1:
            add = 1
        elif self.add == -1 and other.add == 0:
            add = 1
        elif self.add == -1 and other.add == -1:
            pass # impossible

        return Cube(add, \
                    ((max([self.left, other.left]), min([self.right, other.right])),\
                     (max([self.front, other.front]), min([self.back, other.back])), \
                     (max([self.bottom, other.bottom]), min([self.top, other.top]))))

    def __str__(self):
        return f'{self.add}, x={self.left}..{self.right},y={self.front}..{self.back},z={self.bottom}..{self.top}'


with open(sys.argv[1], 'r') as f:
	data = f.readlines()
	
	data = [(1, row[3:].replace('\n', '')) if 'on' in row else (0, row[4:].replace('\n', '')) for row in data]
	
	data = [(i, row.split(',')) for i, row in data]
	
	data = [(i, [tuple(map(int, elem[2:].split('..'))) for elem in row]) for i, row in data]
	
	print(data)

cubes = []

i, elem = data[0]

cubes.append(Cube(i, elem))
total_volume = Cube(i, elem).volume()
print(cubes[0])


for i, elem in data[1:]:
    newCube = Cube(i, elem)
    temp_cubes = []
    temp_volume = 0

    for cube in cubes:
        temp_cube = cube.intersect(newCube)
        if temp_cube != None:
            temp_cubes.append(temp_cube)
            temp_volume += temp_cube.volume()
    cubes.extend(temp_cubes)
    temp_volume += newCube.volume()
    cubes.append(newCube)
    total_volume += temp_volume

print(sum(map(Cube.volume, cubes)))

print(total_volume)
