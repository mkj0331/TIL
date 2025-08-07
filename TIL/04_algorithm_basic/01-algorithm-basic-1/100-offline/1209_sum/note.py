max_res = 0
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

maxx(0, [1,2,252,63,36363,4])
print(max_res)