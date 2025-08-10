import sys
sys.stdin = open('input.txt')

def subtree_size(node):
    if node == 0:
        return 0
    left_size = subtree_size(left[node])
    right_size = subtree_size(right[node])
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
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p
    
    v1_anc = set()
    x = v1
    while x != 0:
        v1_anc.add(x)
        x = parent[x]

    y = v2
    while y not in v1_anc:
        y = parent[y]
    
    lca = y

    ans = subtree_size(lca)

    print(f"#{t} {lca} {ans}")