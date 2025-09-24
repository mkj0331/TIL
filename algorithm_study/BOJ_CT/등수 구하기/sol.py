import sys
sys.stdin = open('input.txt')

'''
N : 현재 랭킹 리스트에 있는 점수의 갯수
score : 태수의 새로운 점수
P: 랭킹 리스트에 올라갈 수 있는 점수의 개수
'''

N, score, P = map(int, input().split())
if N == 0:
    ans = 1
else:
    rank_list = list(map(int, input().split()))
    if (score <= rank_list[-1]) and (N == P):
        ans = -1
    else:
        rank_list.append(score)
        rank_list.sort(reverse=True)
        ans = rank_list.index(score) + 1

print(ans)
