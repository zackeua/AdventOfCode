import sys

def show(img):
    for row in img:
        print(''.join(['.' if elem==0 else '#' for elem in row]))
    print()

def grow(img, n):
    img = [[n, n, n] + row + [n, n, n] for row in img]

    img = [[n]*len(img[0]), [n]*len(img[0]), [n]*len(img[0])] + img + [[n]*len(img[0]), [n]*len(img[0]), [n]*len(img[0])]

    return img

def enhance(img, alg, n_iter):
    n = (n_iter+1)%2

    number = alg[int(''.join([str((n+1)%2)]*9),2)]

    new_img = [[num for num in row] for row in img]
    
    for x_index, row in enumerate(img):
        for y_index, _ in enumerate(row):
            row1 = [None, None, None]
            row2 = [None, None, None]
            row3 = [None, None, None]
            if x_index == 0 and y_index == 0:
                row1[0] = number
                row1[1] = number
                row1[2] = number
                
                row2[0] = number
                row2[1] = img[x_index][y_index]
                row2[2] = img[x_index][y_index+1]

                row3[0] = number
                row3[1] = img[x_index+1][y_index]
                row3[2] = img[x_index+1][y_index+1]

            elif x_index == 0 and y_index == len(img[0])-1:
                row1[0] = number
                row1[1] = number
                row1[2] = number

                row2[0] = img[x_index][y_index-1]
                row2[1] = img[x_index][y_index]
                row2[2] = number
                
                row3[0] = img[x_index+1][y_index-1]
                row3[1] = img[x_index+1][y_index]
                row3[2] = number
            
            elif x_index == 0:
                row1[0] = number
                row1[1] = number
                row1[2] = number

                row2[0] = img[x_index][y_index-1]
                row2[1] = img[x_index][y_index]
                row2[2] = img[x_index][y_index+1]

                row3[0] = img[x_index+1][y_index-1]
                row3[1] = img[x_index+1][y_index]
                row3[2] = img[x_index+1][y_index+1]

            elif x_index == len(img)-1 and y_index == 0:
                row1[0] = number
                row1[1] = img[x_index-1][y_index]
                row1[2] = img[x_index-1][y_index+1]
 
                row2[0] = number
                row2[1] = img[x_index][y_index]
                row2[2] = img[x_index][y_index+1]

                row3[0] = number
                row3[1] = number
                row3[2] = number
                
            elif x_index == len(img)-1 and y_index == len(img[0])-1:
                row1[0] = img[x_index-1][y_index-1]
                row1[1] = img[x_index-1][y_index]
                row1[2] = number

                row2[0] = img[x_index][y_index-1]
                row2[1] = img[x_index][y_index]
                row2[2] = number

                row3[0] = number
                row3[1] = number
                row3[2] = number

            elif x_index == len(img)-1:
                row1[0] = img[x_index-1][y_index-1]
                row1[1] = img[x_index-1][y_index]
                row1[2] = img[x_index-1][y_index+1]

                row2[0] = img[x_index][y_index-1]
                row2[1] = img[x_index][y_index]
                row2[2] = img[x_index][y_index+1]

                row3[0] = number
                row3[1] = number
                row3[2] = number

            elif y_index == 0:
                row1[0] = number
                row1[1] = img[x_index-1][y_index]
                row1[2] = img[x_index-1][y_index+1]

                row2[0] = number
                row2[1] = img[x_index][y_index]
                row2[2] = img[x_index][y_index+1]

                row3[0] = number
                row3[1] = img[x_index+1][y_index]
                row3[2] = img[x_index+1][y_index+1]

            elif y_index == len(img[0])-1:
                row1[0] = img[x_index-1][y_index-1]
                row1[1] = img[x_index-1][y_index]
                row1[2] = number

                row2[0] = img[x_index][y_index-1]
                row2[1] = img[x_index][y_index]
                row2[2] = number

                row3[0] = img[x_index+1][y_index-1]
                row3[1] = img[x_index+1][y_index]
                row3[2] = number
            else:
                row1[0] = img[x_index-1][y_index-1]
                row1[1] = img[x_index-1][y_index]
                row1[2] = img[x_index-1][y_index+1]

                row2[0] = img[x_index][y_index-1]
                row2[1] = img[x_index][y_index]
                row2[2] = img[x_index][y_index+1]

                row3[0] = img[x_index+1][y_index-1]
                row3[1] = img[x_index+1][y_index]
                row3[2] = img[x_index+1][y_index+1]

            pixels = row1 + row2 + row3
            pixels = int(''.join([str(elem) for elem in pixels]), 2)

            new_img[x_index][y_index] = alg[pixels]
    
    return new_img

def get_lit(img):
    return sum([sum(row) for row in img])


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]
    alg = [0 if elem=='.' else 1 for elem in data[0]]
    img = [[0 if elem=='.' else 1 for elem in row] for row in data[2:]]

show(img)
n_iter = 0
times = 50
while n_iter < times*2:
    img = grow(img, 0)
    n_iter += 1
n_iter = 0

while n_iter < times:

    img = enhance(img, alg, n_iter)
    #show(img)
    n_iter += 1
    print(n_iter)


img = img[times:-times]
img = [row[times:-times] for row in img]
#show(img)

print(get_lit(img))