import sys
sys.stdin = open('sample_input (2).txt')


def perm(selected, remain):
    '''
    Args:
        selected: 선택된 값 목록
        reamin: 선택되지 않고 남은 값 목록
    '''
    # 모든 요소를 선택할 것이니... 나머지가 없을때까지
    if not remain:
        res.append(selected)
    else:   # 아직 선택할 수 있는 요소들이 남아 있다면!
        for idx in range(len(remain)):      # 그 요소를 모두 순회하면서
            # idx 번째의 요소를 선택
            select_item = remain[idx]
            # 선택된 idx번째를 제외한 reamin을 만들자. (진짜 나머지 리스트)
            remain_list = remain[:idx] + remain[idx+1:]
            perm(selected + [select_item], remain_list)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # calc[0]부터 [4]까지 +, -, *, /
    calc = list(map(int, input().split()))
    calc_list = []
    for idx, val in enumerate(calc):
        if idx == 0:
            for _ in range(val):
                calc_list.append('+')
        elif idx == 1:
            for _ in range(val):
                calc_list.append('-')
        elif idx == 2:
            for _ in range(val):
                calc_list.append('*')
        else:
            for _ in range(val):
                calc_list.append('/')

    res = []
    perm([], calc_list)

    nums = list(map(int, input().split()))
    res_cases =







