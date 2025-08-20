import sys, heapq
sys.stdin = open("sample_input.txt")

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    vertices = [i for i in range(V+1)]

    adj_list = {v: [] for v in vertices}
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))


    mst = []
    visited = set()
    start_vertex = vertices[0]

    # start_vertex에서 가능한 경로에 대한 (가중치, s, e)를 추가
    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    # print(min_heap)
    while min_heap:
        w, s, e = heapq.heappop(min_heap) # min_heap에서 w가 가장 작은 튜플 셋을 pop
        if e in visited: # 방문한 적이 있다면 넘어가기
            continue

        # 방문한 적이 없다면
        visited.add(e) # 방문 표시
        mst.append((s, e, w))

        for next, weight in adj_list[e]:
            # e를 기준으로 다음으로 향하는 도착 지점이 이미 방문한 지점이면 heap에 추가할 필요도 없음
            if next in visited: continue    # 없어도 되긴 하는데, 효율상 있는게 좋음
            heapq.heappush(min_heap, (weight, e, next))
        # print(min_heap)

    ans = 0
    for i in mst:
        ans += i[2]
    print(f"#{t} {ans}")
