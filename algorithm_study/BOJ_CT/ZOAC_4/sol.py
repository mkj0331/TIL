import sys
sys.stdin = open('input.txt')

'''
# DFS -> 메모리 초과
def DFS(i, j):
    if i>=H or j>=W:
        return
    if mapp[i][j] == 1:
        return

    mapp[i][j] = 1

    DFS(i+M+1, j)
    DFS(i, j+N+1)



H, W, N, M = map(int, input().split())

mapp = [[0]*W for _ in range(H)]

DFS(0, 0)

res = 0
for i in mapp:
    res += sum(i)

print(res)
'''

import math
H, W, N, M = map(int, input().split())
a = math.ceil(W/(M+1))
b = math.ceil(H/(N+1))
print(a*b)