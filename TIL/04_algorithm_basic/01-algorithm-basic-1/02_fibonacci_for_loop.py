def fibonacci_for_loop(n):
    # 기본 룰은 동일하게 적용해야 한다.
    # n이 0이면 0을 반환한다.
    if n == 0:
        return 0
    # n이 1이면 1을 반환한다.
    elif n == 1:
        return 1
    # n이 2 이상인 경우
    else:
        first, second = 0, 1
        # 피보나치 규칙 상, 2,3,4,...,n 까지 있는 수는 필요 없으므로 _ 처리
        for _ in range(2, n+1):
            next_fib = first + second
            first, second = second, next_fib
        # 만약 위의 순회에서 더 이상 다음 연산을 할 작업이 없다면 next_fib == second
        return next_fib


# 사용 예시
print(fibonacci_for_loop(10)) # 55