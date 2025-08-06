import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start):
    # 방문했는지 확인 + 몇 번째로 방문한지를 확인하기 위해 리스트 선언
    visited = [-1] * 101
    # 시작점은 처음에 방문하므로 0으로 변경
    visited[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        for neighbor in adj_list.get(node, []):
            # 연결된 번호를 for문으로 돌면서 해당 번호가 방문하지 않았다면(-1 이라면)
            if visited[neighbor] == -1:
                # 전에 방문했던 visited의 값보다 1 증가시킨 값(깊이 1 추가)으로 넣어줌
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    return visited


for tc in range(1, 11):
    # data_len : 입력받는 데이터의 총 길이, start: 시작 지점
    data_len, start = map(int, input().split())
    data = list(map(int, input().split()))

    # 인접 리스트 만들기
    adj_list = {node: [] for node in range(1, 101)}     # 1~100번 노드
    for i in range(0, data_len, 2):
        u, v = data[i], data[i+1]
        adj_list[u].append(v)

    visited_list = BFS(start)
    # visited_list에서 최대값에 해당하는(마지막으로 연락을 받은) 인덱스이자 지점들 반환
    max_depth_contacted = [i for i, val in enumerate(visited_list) if val == max(visited_list)]
    ans = max(max_depth_contacted) # 그 중에 max
    print(f"#{tc} {ans}")
