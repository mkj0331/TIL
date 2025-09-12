import sys
sys.stdin = open('input.txt')

N = int(input())

if N%2 == 1:
    print('SK')
else:
    print('CY')


