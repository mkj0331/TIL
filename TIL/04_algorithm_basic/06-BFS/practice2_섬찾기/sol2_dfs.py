import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == 0 or visited[nx][ny] == 1:
                continue

            stack.append((nx, ny))
            visited[nx][ny] = 1


# 입력 처리
n, m = map(int, input().split())  # 지도의 크기
arr = [list(map(int, input())) for _ in range(n)]  # 지도 입력
island_cnt = 0  # 섬의 개수
visited = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            DFS(i, j)
            island_cnt += 1

print(island_cnt)