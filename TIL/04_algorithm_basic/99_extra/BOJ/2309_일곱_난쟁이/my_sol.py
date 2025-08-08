import sys
sys.stdin = open('input.txt')
#
# heights = [int(input()) for _ in range(9)]
# ans = None
#
# def dfs(idx, picked, total):
#     global ans
#
#     if total > 100 or len(picked) > 7:
#         return
#     if idx == 9:
#         if len(picked) == 7 and total == 100:
#             ans = sorted(picked)
#         return
#
#     # 선택
#     dfs(idx+1, picked + [heights[idx]], total + heights[idx])
#
#     # 비선택
#     dfs(idx+1, picked, total)
#
# dfs(0, [], 0)
# print(ans)


# DFS
# heights = [int(input()) for _ in range(9)]
#
# ans = None
# def DFS(idx, picked, total):
#     global ans
#     # 키의 총 합이 100보다 크거나, 8명 이상의 난쟁이가 선택된다면
#     if total > 100 or len(picked) > 7:
#         return  # 더 이상 그 조사는 하지 말고 멈추기
#
#     # 9번째 난쟁이(idx==8)까지 조사한 이후에 돌아왔을떄
#     if idx == 9:
#         if total == 100 and len(picked) == 7: # 조건 만족하면
#             ans = sorted(picked) # 답에 저장
#         return  # 9번째 난쟁이까지 다 돌았으면 일단 리턴
#
#     # idx번째 난쟁이를 선택하고 넘어감
#     DFS(idx+1, picked + [heights[idx]], total + heights[idx])
#     # idx번째 난쟁이를 선택하지 않고 넘어감
#     DFS(idx + 1, picked, total)
#
# DFS(0, [], 0)
# print(ans)


# BFS
from collections import deque

heights = [int(input()) for _ in range(9)]

q = deque()
q.append((0, [], 0)) # idx, picked, total

ans = None
while q:
    idx, picked, total = q.popleft()

    if total > 100 or len(picked) > 7:
        continue # 아래를 실행하지 않고 다음 while문으로 넘어감

    if idx == 9:
        if total == 100 and len(picked) == 7:
            ans = sorted(picked)
            break
        continue    # 아래를 실행하지 않고 넘어감

    q.append((idx+1, picked + [heights[idx]], total + heights[idx]))

    q.append((idx + 1, picked, total))

print(*ans, sep ='\n')
