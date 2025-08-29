import sys
sys.stdin = open('input.txt')

import heapq


def distra():
    distances = [float('inf')] * (N+1)
    distances[0] = 0
    visited = set()
    heap = []
    heapq.heappush(heap, (0, 0)) # 시작 거리, 시작 정점

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for next_vertex, next_distance in graph[current_vertex].items():
            acc = current_distance + next_distance
            if acc < distances[next_vertex]:
                distances[next_vertex] = acc
                heapq.heappush(heap, (acc, next_vertex))
    return distances


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = {v: {} for v in range(N+1)}
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    res = distra()
    print(res[N])

