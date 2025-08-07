import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

# 리스트를 최소 힙으로 변환
heapq.heapify(numbers)
print(numbers)

# heap에 -1넣고, 최소 힙에 맞게 위치 반영
heapq.heappush(numbers, -1)
print(numbers)

# 최소 힙의 루트 노트(가장 작은 값) pop
smallest = heapq.heappop(numbers)
print(smallest)

print(numbers)

# 단, 주의 사항
# 이렇게 heap으로 만든 numbers를 리스트처럼 그냥 append 곤란함
# numbers.append(-1)
# print(numbers)