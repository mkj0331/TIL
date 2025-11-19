import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import Counter

N, M = map(int, input().split())
words = []
for _ in range(N):
    temp = input().strip()
    if len(temp) >= M:
        words.append(temp)

cnt = Counter(words)
# (단어, 빈도, 길이) 형태로 리스트 생성
arr = [(word, cnt[word], len(word)) for word in cnt]

# 정렬
arr.sort(key=lambda x: (-x[1], -x[2], x[0]))

# 출력
for word, _, _ in arr:
    print(word)
    
    
# ans = sorted(cnt, key=lambda x: (-cnt[x], -len(x), x)) -> cnt(x)에서 시간초과