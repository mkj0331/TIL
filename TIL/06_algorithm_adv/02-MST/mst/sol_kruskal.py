import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    global parent
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    global parent
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]

    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append([s, e, w])

    edges.sort(key=lambda x: x[2])



    mst = []
    for edge in edges:
        s, e, w = edge
        if find_set(s) != find_set(e):
            union(s, e)
            mst.append(edge)
            # print(parent)

    ans = 0
    for i in mst:
        ans += i[2]
    # print(mst)
    print(f"#{t} {ans}")

