import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
xs = list(map(int, input().split()))

ans = 0

# 처음
ans = max(ans, xs[0] - 0)

# 중간
for i in range(1, M):
    d = xs[i] - xs[i-1]
    ans = max(ans, (d+1)//2)

# 끝
ans = max(ans, N - xs[-1])

print(ans)
