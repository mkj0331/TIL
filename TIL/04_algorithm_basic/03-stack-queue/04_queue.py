# 선입선출
# front - 마지막으로 삭제된 원소(가장 먼저 들어온 원소)
# rear - 저장된 원소 중 마지막 원소(제일 늦게 들어온 원소)
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop(0))
print(queue.pop(0))
print(queue)
print(queue[0])

queue.append(4)
queue.append(5)

print(queue)
queue.append(11)