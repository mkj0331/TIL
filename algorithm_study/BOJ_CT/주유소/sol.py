import sys
sys.stdin = open('input.txt')

N = int(input())
road_len = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

now_price = oil_price[0]
cost = 0
for i in range(N-1):
    if now_price >= oil_price[i]:
        now_price = oil_price[i]
    cost += road_len[i] * now_price
print(cost)