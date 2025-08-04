import sys
sys.stdin = open('sample_input (2).txt')


T = int(input())    # 테스트 케이스 개수
for t in range(1, T+1):

    # 노드 수, 리프 노트 수, 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 노드 수를 idx에 맞춰서 tree 미리 생성
    tree = [None]*(N+1)

    # 리프 노드 값 입력
    for _ in range(M):
        # 노드 번호, 노드 값
        node_num, node_val = map(int, input().split())
        tree[node_num] = node_val

    # 자식 노드의 합을 None에 기입
    # 자식의 값이 채워져 있는 노드의 값부터 채우기
    for idx in range(N-M, 0, -1):
        # 자식 노드가 하나밖에 없는 경우
        if N < idx*2 + 1:
            tree[idx] = tree[idx * 2]

        else:
            # left_child의 idx = idx+2,
            # right_child의 idx = idx*2 + 1
            tree[idx] = tree[idx*2] + tree[idx*2 + 1]

    ans = tree[L] # 노드 번호가 L인 값
    print(f"#{t} {ans}")
