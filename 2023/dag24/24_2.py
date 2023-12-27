import sys
import numpy as np
from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int
    z: int


def sign(number):
    return number / abs(number)


def determinant(point1, point2):
    return point1[0] * point2[1] - point1[1] * point2[0]


def get_position_and_velocity(data):

    p0 = data[0][0]
    p1 = data[1][0]
    p2 = data[2][0]
    v0 = data[0][1]
    v1 = data[1][1]
    v2 = data[2][1]
    # print(p0, p1, p2, v0, v1, v2)

    '''
    p + ti * v = data[i][0] + ti * data[i][1]
    p - data[i][0] = ti * (data[i][1] - v)

    (p - data[i][0]) x (data[i][1] - v) = 0

    i                   j                   k
    p.x - data[i][0].x  p.y - data[i][0].y  p.z - data[i][0].z
    data[i][1].x - v.x  data[i][1].y - v.y  data[i][1].z - v.z

    (p.y - data[i][0].y) * (data[i][1].z - v.z) - (p.z - data[i][0].z) * (data[i][1].y - v.y) = 0
    (p.z - data[i][0].z) * (data[i][1].x - v.x) - (p.x - data[i][0].x) * (data[i][1].z - v.z) = 0
    (p.x - data[i][0].x) * (data[i][1].y - v.y) - (p.y - data[i][0].y) * (data[i][1].x - v.x) = 0

    p.y * data[i][1].z - p.y * v.z - data[i][0].y * data[i][1].z + data[i][0].y * v.z - p.z * data[i][1].y + p.z * v.y + data[i][0].z * data[i][1].y - data[i][0].z * v.y = 0
    p.z * data[i][1].x - p.z * v.x - data[i][0].z * data[i][1].x + data[i][0].z * v.x - p.x * data[i][1].z + p.x * v.z + data[i][0].x * data[i][1].z - data[i][0].x * v.z = 0
    p.x * data[i][1].y - p.x * v.y - data[i][0].x * data[i][1].y + data[i][0].x * v.y - p.y * data[i][1].x + p.y * v.x + data[i][0].y * data[i][1].x - data[i][0].y * v.x = 0



    p.y * v0.z - p.y * v.z - p0.y * v0.z + p0.y * v.z - p.z * v0.y + p.z * v.y + p0.z * v0.y - p0.z * v.y = 0
    p.z * v0.x - p.z * v.x - p0.z * v0.x + p0.z * v.x - p.x * v0.z + p.x * v.z + p0.x * v0.z - p0.x * v.z = 0
    p.x * v0.y - p.x * v.y - p0.x * v0.y + p0.x * v.y - p.y * v0.x + p.y * v.x + p0.y * v0.x - p0.y * v.x = 0


    p.y * v1.z - p.y * v.z - p1.y * v1.z + p1.y * v.z - p.z * v1.y + p.z * v.y + p1.z * v1.y - p1.z * v.y = 0
    p.z * v1.x - p.z * v.x - p1.z * v1.x + p1.z * v.x - p.x * v1.z + p.x * v.z + p1.x * v1.z - p1.x * v.z = 0
    p.x * v1.y - p.x * v.y - p1.x * v1.y + p1.x * v.y - p.y * v1.x + p.y * v.x + p1.y * v1.x - p1.y * v.x = 0

    p.y * v2.z - p.y * v.z - p2.y * v2.z + p2.y * v.z - p.z * v2.y + p.z * v.y + p2.z * v2.y - p2.z * v.y = 0
    p.z * v2.x - p.z * v.x - p2.z * v2.x + p2.z * v.x - p.x * v2.z + p.x * v.z + p2.x * v2.z - p2.x * v.z = 0
    p.x * v2.y - p.x * v.y - p2.x * v2.y + p2.x * v.y - p.y * v2.x + p.y * v.x + p2.y * v2.x - p2.y * v.x = 0


    p.y * v0.z - p.y * v.z - p0.y * v0.z + p0.y * v.z - p.z * v0.y + p.z * v.y + p0.z * v0.y - p0.z * v.y = 0
    -(
    p.y * v1.z - p.y * v.z - p1.y * v1.z + p1.y * v.z - p.z * v1.y + p.z * v.y + p1.z * v1.y - p1.z * v.y = 0
    )

    p.y * v0.z - p0.y * v0.z + p0.y * v.z - p.z * v0.y + p0.z * v0.y - p0.z * v.y
    - p.y * v1.z + p1.y * v1.z - p1.y * v.z + p.z * v1.y - p1.z * v1.y + p1.z * v.y = 0

    p.z * v0.x - p0.z * v0.x + p0.z * v.x - p.x * v0.z + p0.x * v0.z - p0.x * v.z
    - p.z * v1.x + p1.z * v1.x - p1.z * v.x + p.x * v1.z - p1.x * v1.z + p1.x * v.z = 0

    p.x * v0.y - p0.x * v0.y + p0.x * v.y - p.y * v0.x + p0.y * v0.x - p0.y * v.x
    - p.x * v1.y + p1.x * v1.y - p1.x * v.y + p.y * v1.x - p1.y * v1.x + p1.y * v.x = 0

    p.y * v2.z - p0.y * v2.z + p0.y * v.z - p.z * v2.y + p0.z * v2.y - p0.z * v.y
    - p.y * v1.z + p1.y * v1.z - p1.y * v.z + p.z * v1.y - p1.z * v1.y + p1.z * v.y = 0

    p.z * v2.x - p0.z * v2.x + p0.z * v.x - p.x * v2.z + p0.x * v2.z - p0.x * v.z
    - p.z * v1.x + p1.z * v1.x - p1.z * v.x + p.x * v1.z - p1.x * v1.z + p1.x * v.z = 0

    p.x * v2.y - p0.x * v2.y + p0.x * v.y - p.y * v2.x + p0.y * v2.x - p0.y * v.x
    - p.x * v1.y + p1.x * v1.y - p1.x * v.y + p.y * v1.x - p1.y * v1.x + p1.y * v.x = 0


    p.x * ( 0 )
    p.y * ( v0.z -  v1.z )
    p.z * (v1.y - v0.y )
    v.x * ( 0 )
    v.y * ( p1.z - p0.z )
    v.z * ( p0.y - p1.y )
    -b = p0.z * v0.y - p0.y * v0.z + p1.y * v1.z - p1.z * v1.y



    p.x * ( v1.z - v0.z )
    p.y * ( 0 )
    p.z * ( v0.x - v1.x )
    v.x * ( p0.z - p1.z )
    v.y * ( 0 )
    v.z * ( p1.x - p0.x )
    -b = p0.x * v0.z - p0.z * v0.x + p1.z * v1.x - p1.x * v1.z


    p.x * ( v0.y - v1.y )
    p.y * ( v1.x - v0.x )
    p.z * ( 0 )
    v.x * ( p1.y - p0.y )
    v.y * ( p0.x - p1.x )
    v.z * ( 0 )
    -b = p0.y * v0.x - p0.x * v0.y + p1.x * v1.y - p1.y * v1.x


    p.x * ( 0 )
    p.y * ( v0.z - v2.z )
    p.z * ( v2.y - v0.y )
    v.x * ( 0 )
    v.y * ( p2.z - p0.z )
    v.z * ( p0.y - p2.y )
    -b = p0.z * v0.y - p0.y * v0.z + p2.y * v2.z - p2.z * v2.y


    p.x * ( v2.z - v0.z )
    p.y * ( 0 )
    p.z * ( v0.x - v2.x )
    v.x * ( p0.z - p2.z )
    v.y * ( 0 )
    v.z * ( p2.x - p0.x )
    -b = p0.x * v0.z - p0.z * v0.x + p2.z * v2.x - p2.x * v2.z


    p.x * ( v0.y - v2.y )
    p.y * ( v2.x - v0.x )
    p.z * ( 0 )
    v.x * ( p2.y - p0.y )
    v.y * ( p0.x - p2.x )
    v.z * ( 0 )
    -b = p0.y * v0.x - p0.x * v0.y + p2.x * v2.y - p2.y * v2.x

    # M * x - b = 0
    # x = [p.x, p.y, p.z, v.x, v.y, v.z]


    p.x * ( 0 )
    p.y * ( v0.z - v2.z )
    p.z * ( v2.y - v0.y )
    v.x * ( 0 )
    v.y * ( p2.z - p0.z )
    v.z * ( p0.y - p2.y )
    -b = p0.z * v0.y - p0.y * v0.z + p2.y * v2.z - p2.z * v2.y

    '''

    M = [[0, (v0.z - v1.z), (v1.y - v0.y), 0, (p1.z - p0.z), (p0.y - p1.y)],
         [(v1.z - v0.z), 0, (v0.x - v1.x), (p0.z - p1.z), 0, (p1.x - p0.x)],
         [(v0.y - v1.y), (v1.x - v0.x), 0, (p1.y - p0.y), (p0.x - p1.x), 0],
         [0, (v0.z - v2.z), (v2.y - v0.y), 0, (p2.z - p0.z), (p0.y - p2.y)],
         [(v2.z - v0.z), 0, (v0.x - v2.x), (p0.z - p2.z), 0, (p2.x - p0.x)],
         [(v0.y - v2.y), (v2.x - v0.x), 0, (p2.y - p0.y), (p0.x - p2.x), 0]]

    b = [p0.z * v0.y - p0.y * v0.z + p1.y * v1.z - p1.z * v1.y,
         p0.x * v0.z - p0.z * v0.x + p1.z * v1.x - p1.x * v1.z,
         p0.y * v0.x - p0.x * v0.y + p1.x * v1.y - p1.y * v1.x,
         p0.z * v0.y - p0.y * v0.z + p2.y * v2.z - p2.z * v2.y,
         p0.x * v0.z - p0.z * v0.x + p2.z * v2.x - p2.x * v2.z,
         p0.y * v0.x - p0.x * v0.y + p2.x * v2.y - p2.y * v2.x]

    M = np.array(M)
    b = -np.array(b)

    x = np.linalg.solve(M, b)
    x = np.round(x, 0).astype(int)
    return Vector(*x[:3]), Vector(*x[3:])


def main():

    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        data = [[list(map(int, elem.split(',')))
                 for elem in line.strip().split(' @ ')] for line in data]
        data = [[Vector(*elem) for elem in line] for line in data]

        # for line in data:
        #     print(line)

        total = 0
        position, velocity = get_position_and_velocity(data)
        # print(position, velocity)
        total += position.x + position.y + position.z
        print(total)


if __name__ == '__main__':
    main()
