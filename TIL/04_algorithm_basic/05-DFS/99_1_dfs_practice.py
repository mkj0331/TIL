# 그래프 인접 리스트
## 그래프를 탐색할 때는 웬만하면 visited 사용!
graph = {
    'A': ['B', 'C'],    # 0
    'B': ['A', 'D', 'E'],   # 1
    'C': ['A', 'G'],    # 2
    'D': ['B', 'F'],    # 3
    'E': ['B', 'F'],    # 4
    'F': ['D', 'E', 'G'],   # 5
    'G': ['C', 'F']     # 6
}

visited = {node : False for node in graph.keys()}
def dfs(node):
    visited[node] = True
    print(node)

    # 종료 조건 없어도 되나?
    for next in graph[node]:
        if visited[next] == False:
            dfs(next)
    # for val in graph.keys():
    #     if (val in graph[node]) and (visited[val] == False):
    #         dfs(val)
dfs('A')

