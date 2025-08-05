N, K = 7, 3

people = list(range(1, N+1))
output = []
idx = 2
while people:
    output.append(people.pop(idx))
    idx += 3
print(output)
print(people)

# 8 -> 2