import sys
sys.stdin = open('re_sample_input.txt')

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x


def mst_kruskal(edges):
    mst = []
    edges.sort(key = lambda x : x[2])
    for edge in edges:
        s, e, w = edge
        if find_set(s) != find_set(e):
            union(s, e)
            mst.append(edge)
    return mst



T = int(input())
for t in range(1, T+1):
    N = int(input())    # 섬 개수
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    positions = []
    for idx in range(N):
        positions.append([xs[idx], ys[idx]])

    E = float(input())

    parent = [i for i in range(N)]

    edges = []
    for i in range(N):
        for j in range(i+1, N):
            delta_x = positions[i][0] - positions[j][0]
            delta_y = positions[i][1] - positions[j][1]
            w = delta_x**2 + delta_y**2
            edges.append([i, j, w])

    res = mst_kruskal(edges)
    total = 0

    for temp in res:
        total += temp[2]

    ans = E * total

    print(f'#{t} {round(ans)}')