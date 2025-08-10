n_computer = int(input())
n_connection = int(input())
visited = [False]*(n_computer + 1)
nodes = {i : [] for i in range(1, n_computer+1)}
for _ in range(n_connection):
    i, j = map(int, input().split())
    nodes[i].append(j)
    nodes[j].append(i) ## 양방향 그래프!!

def dfs(node):
    visited[node] = True
    
    for next in nodes[node]:
        if visited[next] == False:
            dfs(next)

dfs(1)

print(sum(visited)-1)

