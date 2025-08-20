import sys
sys.stdin = open('sample_input.txt')


# x의 루트 노드 찾는 함수
def find_set(x):
    # 자기 자신이 루트 노드가 아니라면!
    if x != arr[x]:
        # 자기의 대표자의 대표자의...의 대표자를 기입
            # 이 과정에서, 자기의 대표자의 대표자가 있다면, 
            # 그 중간에 있던 대표자도 자신의 대표자로 값을 바꾸면서 경로 평탄화가 됨
        arr[x] = find_set(arr[x])
    return arr[x]


# y를 x의 자식으로 병합하는 함수
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    # x와 y의 루트 노드가 다르다면
    if root_x != root_y:
        # y의 루트노드는 x의 루트노드로 변환
        arr[root_y] = root_x


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # 여기서 arr은 parent와 같음. 즉 arr[i]는 i의 부모 노드 값
    arr = [i for i in range(N+1)]

    for idx in range(0, M*2, 2):
        start = data[idx]
        end = data[idx+1]
        union(start, end)
    
    # 모든 노드에 대해 경로 평탄화
        # 자기 바로 위의 대표자를 향하는 경우들에 대해, 루트 노드(최상단 대표자)로 향하도록 변환
    for i in range(1, N+1):
        find_set(i)
    
    print(f"#{t} {len(set(arr))-1}") # 0은 뺴주기
        

