import sys
sys.stdin = open('sample_input (2).txt')
#
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     product_list = [list(map(int, input().split())) for _ in range(M)]
#
#     capacity = [0] * (N+1)
#
#     for i in range(M):
#         size, price = product_list[i]
#         for w in range(N, size-1, -1):
#             print(w)
#             capacity[w] = max(price + capacity[w-size], capacity[w])
#
#     print(f'#{t} {capacity[N]}')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    datas = [list(map(int, input().split())) for _ in range(M)]

    capacity = [0] * (N+1)

    for data in datas:
        size, price = data

        for i in range(N, size-1, -1):
            capacity[i] = max(capacity[i], price + capacity[i-size])

    print(f"#{t} {capacity[N]}")