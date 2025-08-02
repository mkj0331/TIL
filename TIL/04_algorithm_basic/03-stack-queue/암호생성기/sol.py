import sys
sys.stdin = open('input (1).txt')

# 리스트로 풀어도 되지만, 시간복잡도를 위해 deque 자료구조 사용!
from collections import deque

for _ in range(10):
    tc = int(input())
    nums = deque(map(int, input().split())) # deque로 받아오기

    flag = True  # out - i 가 0일때 while문을 멈추기 위한 Flag
    while flag:
        # 한 사이클 - 5번
        for i in range(1, 6):
            out = nums.popleft()  # front 값 추출
            nums.append(out - i) # rear에 append
            if (out - i) <= 0: # 0 이하면 rear를 음수가 아닌 0으로 바꾸고, for문 멈추고, while문도 멈추기
                flag = False
                nums[-1] = 0
                break
    ans = " ".join(map(str, nums))
    print(f"#{tc} {ans}")
        









