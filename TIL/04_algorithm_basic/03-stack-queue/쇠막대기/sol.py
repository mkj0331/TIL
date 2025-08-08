import sys
sys.stdin = open('sample_input (2).txt')

from collections import deque

def cutter(chars):
    total = 0
    nums = 0
    q = deque(chars)

    while q:
        now = q.popleft()
        if now == '(':
            nums += 1
        else:
            nums -= 1 # 레이저여도, 이전에 레이저의 시작('(')에서 nums +=1 했으니까 -1 해야됨
            if pre == '(': # 레이저면
                total += nums # 현재 있는 막대 수만큼 추가 (막대 수는 마지막에 막대 나갈 때 +1 하면서 나갈거임)
            else:   # 레이저가 아니면 막대 하나가 끝나는 것
                total += 1
        pre = now
    return total


T = int(input())
for t in range(1, T+1):
    chars = input()
    print(f"#{t} {cutter(chars)}")

