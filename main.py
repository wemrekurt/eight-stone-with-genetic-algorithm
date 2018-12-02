from Stone import *

def connections(list, i, j):
    con = [0, 0, 0, 0]
    if i-1 >= 0: con[0] = list[i-1][j]
    if j+1 < 3: con[1] = list[i][j+1]
    if i+1 < 3: con[2] = list[i+1][j]
    if j-1 >= 0: con[3] = list[i][j-1]
    return con

inital_state = [
    [3, 5, 2],
    [1, 6, 8],
    [7, 4, 9]
]

for i, l1 in enumerate(inital_state):
    for j, l2 in enumerate(l1):
        Stone(l2, ((3*i)+j+1), connections(inital_state, i, j))


for stone in Stone.list:
    print stone