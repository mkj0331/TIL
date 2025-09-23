import sys
sys.stdin = open('input.txt')

N = int(input())

data = [list(input()) for _ in range(N)]


def find_star(data):
    for i in range(N):
        for j in range(N):
            if data[i][j] == '*':
                return i, j


head_x, head_y = find_star(data)

heart_x, heart_y = (head_x+1, head_y)

# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이 공백으로 구분해서 출력

temp = ''.join(data[heart_x])

left_arm = heart_y - temp.find('*')
right_arm = temp.rfind('*') - heart_y

waist = 0
for i in range(heart_x + 1, N):
    if data[i][heart_y] == '*':
        waist += 1
    else:
        break


left_leg = 0
for i in range(heart_x + waist + 1, N):
    if data[i][heart_y - 1] == '*':
        left_leg += 1
    else:
        break

right_leg = 0
for i in range(heart_x + waist + 1, N):
    if data[i][heart_y + 1] == '*':
        right_leg += 1
    else:
        break

print(heart_x + 1, heart_y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)
