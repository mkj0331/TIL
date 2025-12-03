import sys
sys.stdin = open('input.txt')

N = int(input())
balances = list(map(int, input().split()))
M = int(input())

if sum(balances) <= M:
    ans = max(balances)
else:
    left, right = 0, max(balances)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        total = sum(min(balance, mid) for balance in balances)

        if total <= M:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1 
            
print(ans)