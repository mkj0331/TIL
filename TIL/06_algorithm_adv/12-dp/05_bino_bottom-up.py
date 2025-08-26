def bino(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)] # n+1 x k+1 2차원 리스트

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    '''
       # 0  1  2  3  4  (k)
        [1, 0, 0, 0, 0] # (x+y)^0
        [1, 1, 0, 0, 0] # (x+y)^1
        [1, 2, 1, 0, 0] # (x+y)^2
        [1, 3, 3, 1, 0] # (x+y)^3
        [1, 4, 6, 4, 1] # (x+y)^4
    '''
    return dp[n][k]


n = 5 
k = 2
print(bino(n, k))  # 출력: 10


