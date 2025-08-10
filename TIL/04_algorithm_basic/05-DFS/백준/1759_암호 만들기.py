import sys
sys.stdin = open('input.txt')

L, C = map(int, input().split())
letters = input().split()
letters.sort()
vowels = set('aeiou')


ans = []
def dfs(idx, pw):

    if idx == C:
         if len(pw) == L:
            v = sum(ch in vowels for ch in pw)
            if v >= 1 and (L - v) >= 2:
                ans.append(pw)
         return

    dfs(idx+1, pw)
    dfs(idx+1, pw + letters[idx])

dfs(0, '')
for i in sorted(ans):
    print(i)