import sys
sys.stdin = open("input.txt")

# 중위 순회 (전역변수 사용 방식)
def inorder_traversal(idx):
    global res
    if idx <= N:
        inorder_traversal(idx * 2)
        res += tree[idx]
        inorder_traversal(idx * 2 + 1)

for t in range(1, 11):  # 테스트 케이스 10개
    N = int(input())
    tree = [None] * (N + 1)  # 트리 초기화


    # 자식 개수별 정점 개수 계산
    child0_cnt = (N // 2) + (N % 2)
    child1_cnt = ((N % 2) + 1) % 2
    child2_cnt = N - child0_cnt - child1_cnt

    # 자식 2개인 정점
    for _ in range(child2_cnt):
        node_num, node_val, child1_num, child2_num = input().split()
        node_num = int(node_num)
        tree[node_num] = node_val

    # 자식 1개인 정점
    for _ in range(child1_cnt):
        node_num, node_val, child1_num = input().split()
        node_num = int(node_num)
        tree[node_num] = node_val

    # 자식 0개인 정점
    for _ in range(child0_cnt):
        node_num, node_val = input().split()
        node_num = int(node_num)
        tree[node_num] = node_val

    res = ''  # 순회 결과 저장할 전역변수 초기화
    inorder_traversal(1)
    print(f"#{t} {res}")