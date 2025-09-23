import sys
sys.stdin = open('input.txt')

N, game = input().split()
N = int(N)

users = set()

for _ in range(N):
    users.add(input())

if game == 'Y':
    ans = len(users)
elif game == 'F':
    ans = len(users) // 2
else:
    ans = len(users) // 3

print(ans)