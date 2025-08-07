import sys
sys.stdin = open('sample_input (2).txt')

import heapq

T = int(input())    # 테스트 케이스 갯수
for t in range(1, T+1):
    max_heap = []   # 최대 힙 담을 리스트
    res = []    # heappop으로 반환된 값 넣을 res

    N = int(input())    # 총 연산 수
    for _ in range(N):
        given = input().split()
        # "연산 1.자연수 x를 삽입"이라면
        if len(given) == 2:
            heapq.heappush(max_heap, -int(given[1]))

        # "연산 2.최대 힙의 루트 노드의 키값을 출력하고, 해당 노드를 삭제"라면
        else:
            # 힙에 값이 있다면
            if max_heap:
                # 루트 노드(가장 큰 값) 반환
                largest = - heapq.heappop(max_heap)
                res.append(largest)
            # 힙에 값이 없다면
            else:
                # -1 반환
                res.append(-1)
    print(f"#{t} {' '.join(map(str, res))}")

