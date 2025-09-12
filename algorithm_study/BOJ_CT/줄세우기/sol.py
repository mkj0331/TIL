import sys
sys.stdin = open('input.txt')

P = int(input())
for t in range(1, P+1):
    heights = list(map(int, input().split()))
    heights.pop(0)

    ans = 0

    lines = [heights.pop(0)]
    while heights:
        now = heights.pop(0)
        for student in lines:
            if student > now:
                ans += 1
        lines.append(now)

    print(f'{t} {ans}')




