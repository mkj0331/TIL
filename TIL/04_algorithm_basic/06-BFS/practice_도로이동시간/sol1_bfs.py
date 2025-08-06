import sys
sys.stdin = open('input.txt')

from collections import deque

#     상  하  좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(x, y):
    # 너비 우선 탐색 -> queue
    # deque의 첫번째 인자는 iterable 객체이고,
    # 내가 지금 queue에 넣고 싶은 후보군은? (0,0)
    queue = deque()
    queue.append((0,0))
    distance[0][0] = 0

    # BFS 탐색
    while queue:    # 후보군이 있는 동안
        x, y = queue.popleft()
        # 이 위치에서 4방향에 대한 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 이제 그 다음 탐색지 data[nx][ny]가 이동 가능한지 판별
            # 1. 리스트의 범위를 벗어나지 않아햐 함
            # 2. 이전에 방문한 적이 없어야 함
            # 3. 그 위치가 길이어야함(1은 길, 0은 벽)
            if 0<=nx<N and 0<=ny<M and distance[nx][ny] == -1 and data[nx][ny]:
                # 위 조건을 모두 만족하면 후보군에 들 수 있다
                queue.append((nx, ny))
                # 다음 위치까지 도달하는 비용은, 내 위치보다 1 증가한 값이다.
                distance[nx][ny] = distance[x][y] + 1
                # 도착지점에 도착하면, BFS 특성상 가장 빠르게 도착한 길이니
                # 그때까지의 비용을 할당하고 종료
                if nx == N-1 and ny == M-1:
                    return
    # 모든 후보군을 다 탐색했지만 return되어서 함수가 종료된 적이 없다면,
    # 코드가 이곳까지 도달했다면 도착할 수 없다는 의미
    return -1

# 데이터 입력
# row: N, col: M
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)] # 101111을 문자열로 받아서 int화 후 list로 -> [1,0,1,1,1,1,]
# 방문 표시를 할거다. -> 우리의 최종 목적이 무엇이냐?
# 해당 위치까지 도달하는데 걸린 비용이 얼만지를 기록!
distance = [[-1]*M for _ in range(N)]
print(data)
print(distance)

get_road_move_time(0, 0)
for dis in distance:
    print(*dis)
print(distance[N-1][M-1])