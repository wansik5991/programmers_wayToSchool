import os
os.system('cls')

import copy

def solution(m, n, puddles):
    m, n = n, m
    map_ = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for x, y in puddles :
        map_[y][x] = -1
    map_[1][1] = 1
    for i in range(1,m+1) :
        for j in range(1,n+1) :
            if map_[i][j] == -1 :
                continue
            if i==1 and j==1 :
                continue
            if map_[i-1][j] != -1 :
                map_[i][j] += map_[i-1][j]
            if map_[i][j-1] != -1 :
                map_[i][j] += map_[i][j-1]
            map_[i][j] %= 1000000007
    return map_[m][n]

print(solution(4,3,[[2, 2]]))
print(solution(100, 100, []), 690285631)