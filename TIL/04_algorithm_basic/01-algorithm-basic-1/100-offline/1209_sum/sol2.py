import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    data = [list(map(int, input().split())) for _ in range(100)]

    # sum_res = 0
    def summ(idx, x):
        global sum_res
        if idx == len(x):
            return
        
        temp = x[idx]
        sum_res += temp
        summ(idx+1, x)



    # max_res = 0
    def maxx(idx, x):
        global max_res
        if idx == len(x):
            return
        
        temp = x[idx]
        if max_res < temp:
            max_res = temp
            maxx(idx+1, x)
        else:
            maxx(idx+1, x)

    # 행
    row_sum_list = []
    for row in data:
        sum_res = 0
        summ(0, row)
        row_sum_list.append(sum_res)

    max_res = 0
    maxx(0, row_sum_list)
    row_max_res = max_res

    # 열
    col_sum_list = []
    for i in range(100):
        temp = 0
        for row in data:
            temp += row[i]
        col_sum_list.append(temp)
    
    max_res = 0
    maxx(0, col_sum_list)
    col_max_res = max_res

    # 대각선 오른쪽 아래방향
    diag_sum_list = []
    temp = 0
    for i in range(100):
        temp += data[i][i]
    diag_sum_list.append(temp)

    # 대각선 왼쪽 아래방향
    temp = 0
    for j in range(100):
        temp += data[j][99-j]
    diag_sum_list.append(temp)

    max_res = 0
    maxx(0, diag_sum_list)
    diag_max_res = max_res


    max_res = 0
    maxx(0, [row_max_res, col_max_res, diag_max_res])
    final_max_res = max_res

    print(f"#{tc} {final_max_res}")



