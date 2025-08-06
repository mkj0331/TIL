data = '100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2'

adj_list = {node : [] for node in list(map(int, data.split()))}
print(adj_list)

not_contacted = list(adj_list.keys())
print(not_contacted)