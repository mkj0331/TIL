import sys
sys.stdin = open('input.txt')

# 공통 조상의 subtree_size 반환 함수
def subtree_size_dfs(node):
    # 자식이 없으면 그 node의 subtree가 없는거니까 0 반환(마지막에 1 더해줘서 return하니까 0)
    if node == 0:
        return 0
    # 왼쪽 subtree 깊이 우선 탐색
        # 왼쪽 자식 노드가 없을 때까지 탐색하고, 그 지점에서 오른쪽 탐색 후 return 1+0+0 (후위순회)
        # 바로 위 노드로 이동해서, 이전에 왼쪽 자식 노드로 이동하느라 탐색하지 못했던 오른쪽 자식을 탐색하고 return 값 반환
    left_size = subtree_size_dfs(left[node])
    # 똑같은 방식으로 오른쪽 subtree 깊이 우선 탐색!
    right_size = subtree_size_dfs(right[node])
    # 본인을 포함(1)한 왼쪽 자식의 subtree + 오른쪽 자식의 subtree
    return 1 + left_size + right_size


T = int(input())
for t in range(1, T+1):
    V, E, v1, v2 = map(int, input().split())
    edges = list(map(int, input().split()))

    left = [0]*(V+1)
    right = [0]*(V+1)
    parent = [0]*(V+1)

    for i in range(0, 2*E, 2):
        p, c = edges[i], edges[i+1]
         # 예 : left[2]의 값은 2번 노드의 왼쪽 자식의 값
        if left[p] == 0:
            left[p] = c
        # 예 : right[4]의 값은 4번 노드의 오른쪽 자식의 값
        else:
            right[p] = c
        # 예 : parent[3]의 값은 3번 노드의 부모의 값
        parent[c] = p

    # v1의 조상들
    v1_anc = set()
    x = v1
    # 조상이 없을 때까지 (parent = [0]*(V+1)이므로 루트노드(1)의 조상도 0으로 저장되어 있음 -> 문제없음)
    while x != 0:
        v1_anc.add(x)
        x = parent[x]
    
    ## # v2의 조상들
    ## v2_anc = set()
    ## x = v2
    ## while x != 0:
    ##     v2_anc.add(x)
    ##     x = parent[x]

    y = v2
    # y가 v1_anc에 등장할 때까지 부모의 부모...
    while y not in v1_anc:
        y = parent[y] # 두둥등장
    least_same_anc = y

    
    ## 교집합에서 가장 큰 수가 가장 큰 공통 조상 노드
    ## least_same_anc = max(v1_anc & v2_anc)

    size = subtree_size_dfs(least_same_anc)

    print(f"#{t} {least_same_anc} {size}")


