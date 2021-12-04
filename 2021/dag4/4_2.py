import sys

boards = []

with open(sys.argv[1], 'r') as f:
    numbers = list(map(int, f.readline().split(',')))

    board = []
    data = f.readlines()
    for i, row in enumerate(data):
        if i % 6 == 0:
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, row.split())))
    boards.append(board)
    boards = boards[1:]

wintime = -1

score = 0

for board in boards:

    check = [[False]*5 for _ in range(5)]
    loop = True
    for niter, number in enumerate(numbers):
        if loop:
            for i in range(5):
                for j in range(5):
                    if number == board[i][j]:
                        check[i][j] = True

            for i in range(5):
                if sum(check[i]) == 5:
                    loop = False
                if sum([check[j][i] for j in range(5)]) == 5:
                    loop = False

            if not loop:
                board_sum = sum([sum([board[i][j] for j in range(5) if not check[i][j]]) for i in range(5)])
                print(board_sum, number)
                if niter > wintime:
                    wintime = niter
                    score = (board_sum) * number


print(score)
