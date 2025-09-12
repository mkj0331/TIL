import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
S = set()
M = int(input())

for _ in range(M):
    given = input().split()

    if given[0] == 'all':
        S = set(range(1,21))
    elif given[0] == 'empty':
        S = set()
    elif given[0] == 'add':
        S.add(int(given[1]))
    elif given[0] == 'remove':
        if int(given[1]) in S:
            S.remove(int(given[1]))
    elif given[0] == 'check':
        if int(given[1]) in S:
            print(1)
        else:
            print(0)
    else:
        if int(given[1]) in S:
            S.remove(int(given[1]))
        else:
            S.add(int(given[1]))
