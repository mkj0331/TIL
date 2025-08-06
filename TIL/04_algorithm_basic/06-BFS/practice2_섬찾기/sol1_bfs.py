import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

# arr[i][j] == 1이고 visited[i][j] == 0인 경우에만 탐색할 BFS 함수 정의
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 움직인 좌표가 지도 벗어났으면 visit하지 말고 for문의 다음으로 넘어가기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 움직인 좌표가 0이면 visit 찍지 말고 넘어가기
            if arr[nx][ny] == 0:
                continue

            # 움직인 좌표가 이미 visit한 곳이면 넘어가기
            if visited[nx][ny] == 1:
                continue

            # 위 3개가 다 아니면 visit하고
            visited[nx][ny] = 1
            # while문 돌릴 queue에 추가
            queue.append((nx, ny))



# 입력 처리
N, M = map(int, input().split())  # 지도의 크기
arr = [list(map(int, input())) for _ in range(N)]  # 지도 입력
island_cnt = 0  # 섬의 개수
visited = [[0] * M for _ in range(N)]


# 지도를 순회하면서
for i in range(N):
    for j in range(M):
        # 섬 땅인 경우에만 BFS 돌려서 그 주위 연결된 섬 땅들 visit처리 후 섬 갯수 +1
        if arr[i][j] == 1 and visited[i][j] == 0:
            BFS(i, j)
            island_cnt += 1
print(island_cnt)



