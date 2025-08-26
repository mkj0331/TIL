from pprint import pprint

import sys
sys.stdin = open('sample_input.txt')
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
pprint(data)
'''
    N X N 크기의 도시에 홈방범 서비스 제공
    서비스 면적은 마름모 모양의 영역에서만 제공됨.
    K가 커질수록 운영 비용이 커짐. K=1 -> 1X1, K=2 -> 3X3, K=3 -> 5X5
    운영 비용(=서비스 면적) : K*K + (K-1)*(K-1)
        1, 5, 13 ,25
'''


def home_security_service(N, M, grid):
    max_houses = 0

    for x in range(N):
        for y in range(N):
            # K는 1부터 N+1까지 시도 가능
            for K in range(1, N + 2):
                houses = 0
                # 마름모 형태 범위 순회
                for dx in range(-K+1, K):
                    dy_range = K - abs(dx) - 1
                    for dy in range(-dy_range, dy_range + 1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                            houses += 1

                cost = K*K + (K-1)*(K-1)
                profit = houses * M

                if profit >= cost:
                    max_houses = max(max_houses, houses)

    return max_houses

