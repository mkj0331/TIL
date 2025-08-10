def comb(current_comb, start_idx):
    if len(current_comb) == r:
        ans.append(current_comb)
        return
    
    for idx in range(start_idx, len(arr)):
        current_comb.append(arr[idx])

        comb(current_comb, idx+1)

        comb.pop()

arr = [1,2,3,4]
ans = []
r = 3
