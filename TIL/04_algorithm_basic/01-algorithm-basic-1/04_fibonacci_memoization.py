def fibonacci_memoization(n):
    # n이 2 이상이고, memo[n]번째가 아직 계산되지 않았으면 계산하기.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci_memoization(n-2) + fibonacci_memoization(n-1)
    return memo[n]

# 피보나치 수 10까지의 결과를 기록하고 싶다.
n = 10
# 10개의 값을 기록하는 List
memo = [0]*(n+1)    # 0번부터 10번까지니까 총 11개
# 피보나치 기본 룰
memo[0], memo[1] = 0, 1
print(memo)

print(fibonacci_memoization(n))