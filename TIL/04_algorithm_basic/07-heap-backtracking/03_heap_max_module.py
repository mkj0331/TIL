import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

max_heap = []
for number in numbers:
    heapq.heappush(max_heap, -number)

print(max_heap) # max_heap을 각 원소에 -1을 붙인 채로 반환

largest = -heapq.heappop(max_heap) # 반환할 때 - 붙여서 반환
print(largest)

