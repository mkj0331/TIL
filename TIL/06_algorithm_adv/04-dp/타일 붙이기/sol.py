T = int(input())
for t in range(1, T+1):
    N = int(input())

    dp = [0]*(N+1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6
    for i in range(4, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2] + dp[i-3]

    print(f'#{t} {dp[N]}')