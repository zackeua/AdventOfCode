import sys

import numpy as np
from stl import mesh


def get_z(c):
    if c == 'S':
        c = 'a'
    if c == 'E':
        c = 'z'
    return ord(c) - 96

def get_vertices(x, y, z):
    return np.array([[x, y, 0],
                     [x+1, y, 0],
                     [x+1, y+1, 0],
                     [x, y+1, 0],
                     [x, y, z],
                     [x+1, y, z],
                     [x+1, y+1, z],
                     [x, y+1, z]])

def get_faces(x, y, z):
    return np.array([[0,3,1],
                     [1,3,2],
                     [0,4,7],
                     [0,7,3],
                     [4,5,6],
                     [4,6,7],
                     [5,1,2],
                     [5,2,6],
                     [2,3,6],
                     [3,7,6],
                     [0,1,5],
                     [0,5,4]])


def example():
    # Define the 8 vertices of the cube
    vertices = np.array([\
        [-1, -1, -1],
        [+1, -1, -1],
        [+1, +1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
        [+1, -1, +1],
        [+1, +1, +1],
        [-1, +1, +1]])

    # Define the 12 triangles composing the cube
    faces = np.array([\
        [0,3,1],
        [1,3,2],
        [0,4,7],
        [0,7,3],
        [4,5,6],
        [4,6,7],
        [5,1,2],
        [5,2,6],
        [2,3,6],
        [3,7,6],
        [0,1,5],
        [0,5,4]])

    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]

    # Write the mesh to file "cube.stl"
    cube.save('cube.stl')


def main():

    side_length = 1
    with open(sys.argv[1], 'r') as f:
        faces = get_faces(0, 0, 0)
        data = f.readlines()
        data = [row.replace('\n', '') for row in data]
        length = len(data)
        width = len(data[0])
        print(faces.shape[0])
        print(length)
        print(width)
        STL_MESH = mesh.Mesh(np.zeros(faces.shape[0] * length * width, dtype=mesh.Mesh.dtype))
        for x, row in enumerate(data):
            for y, elem in enumerate(row):
                z = get_z(elem)
                vertecies = get_vertices(x, y, z)
                for i, f in enumerate(get_faces(x, y, z)):
                    for j in range(3):
                        STL_MESH.vectors[x * width + y + i][j] = vertecies[f[j], :]
        print(STL_MESH.vectors)
        STL_MESH.save('cube.stl')


if __name__ == '__main__':
    main()