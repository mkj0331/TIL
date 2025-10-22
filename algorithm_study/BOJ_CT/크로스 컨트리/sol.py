import sys
from collections import Counter
sys.stdin = open('input.txt')

# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    counter = Counter(teams)
    scores = {}

    rank = 1
    for i in range(N):
        if counter[teams[i]] == 6:
            if teams[i] in scores:
                scores[teams[i]].append(rank)
            else:
                scores[teams[i]] = [rank]
            rank += 1

    print((sorted(scores, key=lambda x: (sum(scores[x][0:4]), scores[x][4])))[0])





# T = int(input())
# for _ in range(T):
#     N = int(input())
#     teams = list(map(int, input().split()))
#     counter = Counter(teams)
#     scores = {}
#
#     rank = 1
#     for i in range(N):
#         if counter[teams[i]] == 6:
#             if teams[i] in scores:
#                 scores[teams[i]].append(rank)
#             else:
#                 scores[teams[i]] = [rank]
#             rank += 1
#
#     # print(scores)
#     print(sorted(scores, key=lambda x: (sum(scores[x][0:4]), scores[x][4]))[0])
#     # 먼저 앞 4개 합이 작은 순,
#     # 같다면 5번째 값이 작은 순으로 정렬됩니다.
