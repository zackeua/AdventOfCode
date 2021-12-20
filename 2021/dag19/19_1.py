import sys



def tup_add(tup1, tup2):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1], tup1[2] + tup2[2])

def tup_sub(tup1, tup2):
    return (tup1[0] - tup2[0], tup1[1] - tup2[1], tup1[2] - tup2[2])

def tup_mul(tup1, tup2):
    return (tup1[0] * tup2[0], tup1[1] * tup2[1], tup1[2] * tup2[2])

def tup_index(tup1, tup2):
    return (tup1[tup2[0]-1], tup1[tup2[1]-1], tup1[tup2[2]-1])

def get_order(tup, tup2):
    x, y, z = tup2
    if tup == (x, y, z): return (1, 2, 3), (1, 1, 1)
    if tup == (x, -z, y): return (1, 3, 2), (1, -1, 1)
    if tup == (x, -y, -z): return (1, 2, 3), (1, -1, -1) 
    if tup == (x, z, -y): return (1, 3, 2), (1, 1, -1)
    
    if tup == (-x, y, -z): return (1, 2, 3), (-1, 1, -1)
    if tup == (-x, -z, -y): return (1, 3, 2), (-1, -1, -1)
    if tup == (-x, -y, z): return (1, 2, 3), (-1, -1, 1)
    if tup == (-x, z, y): return (1, 3, 2), (-1, 1, 1)
    
    if tup == (y, z, x): return (2, 3, 1), (1, 1, 1)
    if tup == (y, -x, z): return (2, 1, 3), (1, -1, 1)
    if tup == (y, -z, -x): return (2, 3, 1), (1, -1, -1) 
    if tup == (y, x, -z): return (2, 1, 3), (1, 1, -1)
    
    if tup == (-y, z, -x): return (2, 3, 1), (-1, 1, -1)
    if tup == (-y, -x, -z): return (2, 1, 3), (-1, -1, -1)
    if tup == (-y, -z, x): return (2, 3, 1), (-1, -1, 1)
    if tup == (-y, x, z): return (2, 1, 3), (-1, 1, 1)

    if tup == (z, x, y): return (3, 1, 2), (1, 1, 1)
    if tup == (z, -y, x): return (3, 2, 1), (1, -1, 1)
    if tup == (z, -x, -y): return (3, 1, 2), (1, -1, -1) 
    if tup == (z, y, -x): return (3, 2, 1), (1, 1, -1)
    
    if tup == (-z, x, -y): return (3, 1, 2), (-1, 1, -1)
    if tup == (-z, -y, -x): return (3, 2, 1), (-1, -1, -1)
    if tup == (-z, -x, y): return (3, 1, 2), (-1, -1, 1)
    if tup == (-z, y, x): return (3, 2, 1), (-1, 1, 1)



def match_xyz(tup, x,y,z):
    if tup == (x, y, z): return True
    if tup == (x, -z, y): return True
    if tup == (x, -y, -z): return True
    if tup == (x, z, -y): return True
    
    if tup == (-x, y, -z): return True
    if tup == (-x, -z, -y): return True
    if tup == (-x, -y, z): return True
    if tup == (-x, z, y): return True
    
    return False

def match(tup1, tup2):
    x, y, z = tup2

    if match_xyz(tup1, x,y,z): return True
    if match_xyz(tup1, y,z,x): return True
    if match_xyz(tup1, z,x,y): return True

    return False

def to_vec(tups):
    result = []
    for i, coord1 in enumerate(tups):
        for j, coord2 in enumerate(tups):
            if i > j: result.append((tuple([a-b for a, b in zip(coord1, coord2)]), coord1, coord2))
    return result


with open(sys.argv[1], 'r') as f:
    data = f.readlines()

scanners = []

parse = False
for line in data:
    if line == '\n':
        parse = False
        scanners.append(coords)
    
    if parse:
        coords.append(tuple(map(int, line.split(','))))

    if line[:3] == '---':
        parse = True
        coords = []
scanners.append(coords)


beacons = scanners[0]

u = {b:1 for b in beacons}

queue = [i for i in range(len(scanners))][1:]

while queue != []:
    index = queue[0]
    print(queue)
    queue = queue[1:]
    index_coords = scanners[index] # list of coordinates in frame of scanner index
    # calculate overlap
    beacon_vectors = to_vec(beacons) # N*(N-1)/2 vectors with no offset dependancy
    index_vectors = to_vec(index_coords)
    matched_coords = []
    for beacon_diff, beacon_a, beacon_b in beacon_vectors:
        for index_diff, index_a, index_b in index_vectors:
            if match(beacon_diff, index_diff):
                if (beacon_a, index_a) not in matched_coords: matched_coords.append((beacon_a, index_a))
                if (beacon_b, index_b) not in matched_coords: matched_coords.append((beacon_b, index_b))
            if len(matched_coords) >= 11: break
    
    if len(matched_coords) >= 11:
        # map matched_coords to 0:s of reference
        diff_beacon = to_vec([matched_coords[0][0], matched_coords[1][0]])
        diff_index = to_vec([matched_coords[0][1], matched_coords[1][1]])
        order, sign = get_order(diff_beacon[0][0], diff_index[0][0])
        
        mapping = lambda tup: tup_mul(sign, tup_index(tup, order))

        diff = tup_sub(matched_coords[0][0], mapping(matched_coords[0][1]))
        
        mapping = lambda tup: tup_add(tup_mul(sign, tup_index(tup, order)), diff)
        
        # add non overlapping beacons to 0:s frame
        for cord in [mapping(coord) for coord in index_coords]:
            if cord not in beacons: beacons.append(cord)
           
            
    else:
        queue.append(index)


print(len(beacons))
