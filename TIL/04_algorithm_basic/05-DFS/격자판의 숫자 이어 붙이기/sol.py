import sys
sys.stdin = open('sample_input (2).txt')

def dfs(row, col, num):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    num += data[row][col] # dfs 한번 돌 때마다 종료 조건에 가까워지도록 추가
    if len(num) == 7: # dfs 종료 조건 먼저 생각!
        result.append(num)
        return # dfs 종료
    for i in range(4):
        # 완전 탐색
        # 위아래왼오 모든 경우에 대해 dfs 돌려서 결과에 추가
        if 0<=row+dx[i]<4 and 0<=col+dy[i]<4:
            dfs(row+dx[i], col+dy[i], num)


T = int(input())
for tc in range(1, T+1):
    data = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for x in range(4):
        for y in range(4):
            dfs(x, y, '') # 임의의 시작점 케이스 전부 실행

    answer = len(set(result))
    print(f"#{tc} {answer}")