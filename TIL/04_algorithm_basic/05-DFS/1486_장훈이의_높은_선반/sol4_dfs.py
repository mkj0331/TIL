# import sys
# sys.stdin = open("input.txt")

# def dfs(idx, total):
#     global min_height
#     # 내 최종 결과가 min_height가 작아지길 바라는건데
#     # 이미 지금까지 더해 나간 총합이 min_height보다 크면...
#     # 아직 점원이 남았어도 점원의 키를 더해볼 필요가 있을까?
#     # 점원의 키가 음수일 가능성은 없지 않음?
#     if total >= min_height:
#         return


#     # 현재 탐색 중인 점원의 index
#     # 지금까지 선택한 점원들의 키

#     # idx가 얼마가 되면 종료? N
#     if idx == N:
#         # 지금까지 선택된 점원들의 키의 총합이
#         if total >= B:
#             min_height = min(min_height, total)
#         return
#     # 아직 모든 점원에 대해서 탐색하지 않았으므로,
#     dfs(idx+1, total + arr[idx]) #idx의 키를 total에 더하기로 결정했을 때의 dfs
#     # 이번 점원의 키는 더하지 않는다.
#     dfs(idx+1, total) #idx의 키를 total에 더하지 않기로 결정했을 때의 dfs


# T = int(input())
# for tc in range(1, T + 1):
#     # N: 사람 수, B: 목표 높이
#     N, B = map(int, input().split())
#     # 각 사람의 키를 입력 받아 리스트로 저장
#     arr = list(map(int, input().split()))

#     # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
#     min_height = 10000 * N 

#     dfs(0, 0)
#     # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
#     print(f"#{tc} {min_height - B}")


import sys
sys.stdin = open('input.txt')

def dfs(idx, total):
    global ans

    # idx가 끝까지 도달(끝까지 조사) 전에, 이미 total이 ans보다 크다면, 
    # 굳이 다음 인덱스로 넘어가면서 추가로 조사할 필요가 없음
    if total > ans:
        return

    # 끝까지 조사 했으면(각각의 점원에 대해서 선택한 경우와 선택하지 않은 경우 모두 조사)    
    if idx == N:
        # 선반의 높이보다 크다면
        if total >= B:
            # 최소값 비교해서 입력
            ans = min(ans, total)
        # 다음 idx로 넘어가서 indexError 나지 않게 리턴 (idx가 하나씩 넘어가면서 dfs 조사할 때 웬만하면 종료 조건은 이런 식)
        return

    # 해당 idx의 점원을 선택한 경우
    dfs(idx+1, total + heights[idx])
    # 해당 idx의 점원을 선택하지 않은 경우
    dfs(idx+1, total)


T = int(input())
for t in range(1, T+1):
    # N : 점원 수, B : 선반의 높이
    N, B = map(int, input().split()) 
    heights = list(map(int, input().split()))

    ans = N*10000
    dfs(0, 0)
    print(f"#{t} {ans - B}")