# Bottom-Up 방식 -> 이게 더 좋은듯?
# 작은 문제부터 차근차근 답을 구해나가는 방식   
# 이건 재귀를 안쓰고 반복문으로 구현해서 더 직관적!

# 동적 계획법 => 메모이제이션(Top-Down) / 타뷸레이션(Bottom-Up)

def fibo(N):
    if N <= 1:
        return N
    
    # 함수 내에서 저장할 공간을 생성
    dp = [0] * (N + 1)
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[N]

print(fibo(100)) 