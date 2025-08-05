# N, K = 7, 3

# people = list(range(1, N+1))
# output = []
# idx = 0 
# # idx = 2 -> 4 -> 1 -> 3 -> 2 -> 0 -> 0
# while people:
#     idx = (idx + K - 1) % len(people)
#     output.append(people.pop(idx))

# res = ", ".join(map(str, output))
# print(f"<{res}>")

N, K = map(int, input().split())

people = list(range(1, N+1))
output = []
idx = 0
while people:
    idx = (idx + K - 1) % len(people)
    output.append(people.pop(idx))

res =  ", ".join(map(str, output))
print(f"<{res}>")