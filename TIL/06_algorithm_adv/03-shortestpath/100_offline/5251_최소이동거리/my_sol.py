import sys
sys.stdin = open('input.txt')

import heapq

def distra():
    distances = [float('inf')] * (N+1)
    visited = set()
    heap = []
    # 누적 거리, 시작 정점
    heapq.heappush(heap, (0, 0))
    distances[0] = 0

    while heap:
        weight, current = heapq.heappop(heap)
        if current in visited: continue
        visited.add(current)

        for next, next_weight in graph[current].items():
            acc = weight + next_weight
            if acc < distances[next]:
                distances[next] = acc
                heapq.heappush(heap, (acc, next))
    return distances

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]

    graph = {v: {} for v in range(N+1)}
    for s, e, w in data:
        graph[s][e] = w

    res = distra()
    print(f'#{t} {res[N]}')
