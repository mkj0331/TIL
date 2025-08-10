# from pprint import pprint
import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if mapp[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)
            

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    mapp = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        mapp[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False]*M for _ in range(N)]
                
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mapp[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                cnt += 1
    print(cnt)