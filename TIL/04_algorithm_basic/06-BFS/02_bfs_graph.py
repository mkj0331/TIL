from collections import deque

def BFS(start_vertex):
    # 해당 정점 방문 여부를 표시할 배열이 하나 필요
    # visited = [0] * len(nodes)
    visited = set()
    # 후보군을 저장
    # deque는 첫번째 인자로 iterable 객체를 받는다
    queue = deque([start_vertex])
    visited.add(start_vertex)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 내 인접 리스트에서 인접 정점 찾아서 순회
        for neighbor in adj_list.get(node, []):
            # 해당 정점 아직 방문한 적이 없다면
            if neighbor not in visited:
                visited.add(neighbor) # 방문 예정 표시
                queue.append(neighbor)
    return result

# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 4',
    '3 5',
    '4 5',
    '5 6'
]

# 인접 리스트 형태
'''
adj_list = {
    'A': ['B','C'],
    ...
    'G':['F'],
}
'''
adj_list = {node: [] for node in nodes}
# print(adj_list)
# 간선 정보와 정점의 index 정보로 adj_list 채워주기
for edge in edges:
    u, v = edge.split()     # 시작 정점, 도착 정점
    # print(f'{u}: {nodes[int(u)]}, {v}: {nodes[int(v)]}')
    adj_list[nodes[int(u)]].append(nodes[int(v)])
    # 현재 간선 정보는 양쪽으로 다 갈 수 있는 무방향 그래프
    adj_list[nodes[int(v)]].append(nodes[int(u)])

print(adj_list)



# 인접 행렬 => [[], [], [], ...]
adj_matrix = [[0]*len(nodes) for _ in range(len(nodes))]
# print(adj_matrix)
for edge in edges:
    u, v = edge.split()
    u_index, v_index = int(u), int(v)
    # print(u_index, v_index)
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1
print(adj_matrix)

print(BFS('A'))



