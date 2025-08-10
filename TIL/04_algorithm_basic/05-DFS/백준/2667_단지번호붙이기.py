import sys
sys.stdin = open('input.txt')
from pprint import pprint

N = int(input())
mapp = []
for _ in range(N):
    mapp.append(list(map(int, list(input()))))

visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

house_cnt_list = []
house_cnt = 0
def dfs(x, y):
    global house_cnt, house_cnt_list
    visited[x][y] = True
    house_cnt += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if mapp[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)
            

total = 0
for x in range(N):
    for y in range(N):
        if mapp[x][y] == 1 and visited[x][y] == False:
            dfs(x,y)
            total += 1
            house_cnt_list.append(house_cnt)
            house_cnt = 0

print(total)
for val in sorted(house_cnt_list):
    print(val)