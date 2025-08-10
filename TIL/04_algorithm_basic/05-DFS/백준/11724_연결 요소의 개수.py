import sys
sys.setrecursionlimit(10**6)  # (필요하면)
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False]*(N+1)
nodes = {i : [] for i in range(1, N+1)}
for _ in range(M):
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i)

def dfs(node):
    visited[node] = True

    for next in nodes[node]:
        if visited[next] == False:
            dfs(next)


cnt = 0
while False in visited[1:]:
    node = visited[1:].index(False) + 1
    dfs(node)
    cnt += 1
        
print(cnt)