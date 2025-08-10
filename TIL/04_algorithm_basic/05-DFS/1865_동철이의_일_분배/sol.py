import sys
sys.stdin = open('input2.txt')

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)] # 이게 인접 리스트?

visited