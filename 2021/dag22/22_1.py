import sys

d = {}

def get_count(d, cond=True):
	return sum([d[k] for k in d if cond(k)])

with open(sys.argv[1], 'r') as f:
	data = f.readlines()
	
	data = [(1, row[3:].replace('\n', '')) if 'on' in row else (0, row[4:].replace('\n', '')) for row in data]
	
	data = [(i, row.split(',')) for i, row in data]
	
	data = [(i, [tuple(map(int, elem[2:].split('..'))) for elem in row]) for i, row in data]
	
	print(data)
	
n = 50
condition = lambda k: -n <= k[0] <= n and -n <= k[1] <= n and -n <= k[2] <= n




for i, elem in data:
	print(i, elem)
	x_min = max([elem[0][0], -n])
	x_max = min([elem[0][1], n])
	y_min = max([elem[1][0], -n])
	y_max = min([elem[1][1], n])
	z_min = max([elem[2][0], -n])
	z_max = min([elem[2][1], n])
	
	if condition((x_min, y_min, z_min)) and condition((x_max, y_max, z_max)):
		for x in range(x_min, x_max+1):
			for y in range(y_min, y_max+1):
				for z in range(z_min, z_max+1):
					if i or (x, y, z) in d and condition((x, y, z)):
						d[(x, y, z)] = i

print(get_count(d, condition ))