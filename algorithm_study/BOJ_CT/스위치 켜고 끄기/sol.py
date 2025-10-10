import sys
sys.stdin = open('input.txt')

N = int(input()) # 스위치의 개수
switches = list(map(int, input().split()))
switches.insert(0, -1)
n_students = int(input())

for _ in range(n_students):
    gender, num = map(int, input().split())
    if gender == 1: # 남
        for i in range(num, N+1, num):
            switches[i] = (switches[i] + 1) % 2

    elif gender == 2: # 여
        temp = 0
        while True:
            if (num-(temp+1) < 1) or (num+(temp+1) > N):
                break

            if switches[num-(temp+1)] == switches[num+(temp+1)]:
                temp += 1
            else:
                break
        for j in range(num-temp, num+temp+1):
            switches[j] = (switches[j]+1) % 2

for i in range(1, N+1, 20):
    print(' '.join(map(str, switches[i:i+20])))

