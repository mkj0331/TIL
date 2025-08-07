import sys
sys.stdin = open('sample_input (2).txt')

# from itertools import combinations
#
# T = int(input())    # 테스트 케이스 수
# for t in range(1, T+1):
#     N, L = map(int, input().split())
#     scores = []     # 재료에 대한 점수 담을 리스트
#     cals = []   # 해당 재료의 칼로리를 담을 리스트
#
#     for _ in range(N):  # 점수, 칼로리 입력
#         temp = list(map(int, input().split()))
#         scores.append(temp[0])
#         cals.append(temp[1])
#
#     max_score = 0   # max_score 낮은 값으로 미리 설정
#     for r in range(1, N+1):
#         for comb in combinations(range(N), r):
#             total_score = sum(scores[i] for i in comb)
#             total_cal = sum(cals[i] for i in comb)
#             if total_cal <= L:
#                 max_score = max(max_score, total_score)
#
#     print(f"#{t} {max_score}")



def DFS(idx, now_score, now_cal):
    global max_score

    # 칼로리가 L 넘으면 더 이상 조사하지 않고 끝냄
    if now_cal > L:
        return

    # 칼로리가 L이 넘지 않은 상태로 조사 마지막까지 도달했으면
    if idx == N:
        # max_score와 비교하기
        max_score = max(max_score, now_score)
        return

    # 해당 재료를 선택하지 않지 않고 다음 재료로 넘어감
    DFS(idx + 1, now_score, now_cal)
    # 해당 재료를 선택하고 다음 재료로 넘어감
    DFS(idx + 1, now_score + scores[idx], now_cal + cals[idx])


T = int(input())    # 테스트 케이스 수
for t in range(1, T+1):
    N, L = map(int, input().split())
    scores = []     # 재료에 대한 점수 담을 리스트
    cals = []   # 해당 재료의 칼로리를 담을 리스트

    for _ in range(N):  # 점수, 칼로리 입력
        temp = list(map(int, input().split()))
        scores.append(temp[0])
        cals.append(temp[1])

    max_score = 0
    DFS(0, 0, 0)
    print(f"#{t} {max_score}")









