import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

N, S = map(int, input().split())
data = list(map(int, input().split()))


def dfs(idx, total):
    global case
    
    if idx == N:
        if total == S:
            case += 1
        return
    
    dfs(idx+1, total)
    dfs(idx+1, total+data[idx])

case = 0
dfs(0, 0)
if S == 0:
    case -= 1
print(case)