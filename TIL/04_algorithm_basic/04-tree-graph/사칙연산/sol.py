import sys
sys.stdin = open('input.txt')

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b

for t in range(1, 11):
    N = int(input())
    tree = [None] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        parts = input().split()
        idx = int(parts[0])
        if len(parts) == 2:
            tree[idx] = parts[1]
        else:
            tree[idx] = parts[1]
            left[idx] = int(parts[2])
            right[idx] = int(parts[3])

    def postorder(idx):
        if left[idx] == 0 and right[idx] == 0:
            return float(tree[idx])
        a = postorder(left[idx])
        b = postorder(right[idx])
        return calculator(a, b, tree[idx])

    result = postorder(1)
    print(f"#{t} {int(result)}")
