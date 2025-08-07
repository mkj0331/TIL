# sys
import sys
# open을 사용해서 input 파일을 연다
sys.stdin = open('input.txt')

# # 이 문제는 10개의 Test Case를 가진다
# for _ in range(10):
#     tc = int(input())    # 테스트케이스 번호 입력
#
#     # 100 x 100을 2차원 리스트로 받아야 한다.
#     # 즉, 한 번 입력받은 한 줄에 100개의 숫자가 공백을 기준으로 문자열로 오게 됨
#         # 이걸 100번 반복해야함
#     data = [list(map(int, input().split())) for _ in range(100)]
#     # print(data)
#     # 각 행마다 가진 값들을 더한다.
#     row_sums = [sum(x) for x in data]
#     # 각 열마다 가진 값들을 더한다.
#     col_sums = []
#     for _ in range(100):
#         temp = 0
#         for i in range(100):
#             temp +=
#
#     # 대각선의 값들을 더한다.
#     # 그 모든 값들 중 제일 큰 값을 구한다. -> max 금지

T = int(input())
mapp = [list(map(int, input().split())) for _ in range(100)]
print(mapp)

