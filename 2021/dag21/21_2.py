import sys

def rand():
    '''
    [1+1+1, 1+1+2, 1+1+3, 1+2+1, 1+2+2, 1+2+3, 1+3+1, 1+3+2, 1+3+3
    2+1+1, 2+1+2, 2+1+3, 2+2+1, 2+2+2, 2+2+3, 2+3+1, 2+3+2, 2+3+3,
    3+1+1, 3+1+2, 3+1+3, 3+2+1, 3+2+2, 3+2+3, 3+3+1, 3+3+2, 3+3+3]
    '''
    #return [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]
    #return [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 9]
    return [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


d = {}

def play(i):
    if i in d: return d[i]

    score, pos, player, count = i
    score = list(score)
    pos = list(pos)
    player = player
    count = list(count)

    # end recursion
    if score[0] >= s[0]:
        d[i] = (1, 0)
        #print((1, 0))
        return (1, 0)
    if score[1] >= s[0]:
        d[i] = (0, 1)
        #print((0, 1))
        return (0, 1)
    
    # copy scores to be able to recurse
    temp_score = score.copy()
    temp_pos = pos.copy()
    steps = rand()
    local_count = [0, 0]
    for step, c in steps:
        temp_pos[player] = (pos[player] + step)%10
        # add score
        temp_score[player] = score[player] + temp_pos[player] + 1
        temp_count = count.copy()
        #temp_count[player] += c
        
        temp_count = play((tuple(temp_score), tuple(temp_pos), not player, tuple(temp_count)))
          
        local_count[0] += temp_count[0]*c
        local_count[1] += temp_count[1]*c

    #print(local_count)
    d[i] = local_count
    return local_count


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [row.replace('\n', '') for row in data]
    pos = [0, 0]
    data = [row.split(':') for row in data]
    pos[0] = int(data[0][1])-1
    pos[1] = int(data[1][1])-1


player = 0

s = [21]

count = play(((0, 0), tuple(pos), player, (0, 0)))

print(max(count))