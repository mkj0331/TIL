import sys
sys.stdin = open('input.txt')
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    # 암호 코드가 포함된 row 추출
    row_with_pw = None
    for row in data:
        if '1' in row:
            row_with_pw = row
            break

    # 그 row에서 암호코드만 추출
    finish_index = row_with_pw.rfind('1') + 1
    start_index = finish_index-56
    pw_code = row_with_pw[start_index:finish_index]

    # 해당 암호코드를 7개의 비트로 이루어진 8개의 원소로 분리
    code_nums = []
    for i in range(0, len(pw_code), 7):
        code_nums.append(pw_code[i:i+7])

    # 그림에 주어진 암호화 규칙
    rule = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    # 암호를 숫자로 해독한 리스트
    final_code_nums = []
    for val in code_nums:
        final_code_nums.append(rule[val])

    # 홀수번째 숫자
    hol = final_code_nums[0:7:2]

    # 짝수번째 숫자
    jjak = final_code_nums[1:8:2]

    # 올바른 암호코드라면
    if ((sum(hol)*3 + sum(jjak)) % 10) == 0:
        ans = sum(final_code_nums) # 숫자 합
    # 잘못된 암호코드라면
    else:
        ans = 0 # 0

    print(f'#{t} {ans}')